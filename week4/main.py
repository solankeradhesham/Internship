"""E-commerce sales analysis: clean, analyze, visualize, and report."""
from pathlib import Path
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
CHART_DIR = BASE_DIR / "visualizations"
REPORT_DIR = BASE_DIR / "report"

def load_and_clean_data(path: Path) -> tuple[pd.DataFrame, dict]:
    """Load CSV, validate required fields, and remove invalid/duplicate records."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    required = {"order_date", "category", "product", "city", "quantity", "unit_price", "discount"}
    missing_columns = required - set(df.columns)
    if missing_columns:
        raise ValueError("Missing required columns: " + ", ".join(sorted(missing_columns)))

    original_rows = len(df)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    for col in ["quantity", "unit_price", "discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop_duplicates()
    after_duplicates = len(df)
    df = df.dropna(subset=["order_date", "category", "product", "city", "quantity", "unit_price"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]
    df["discount"] = df["discount"].fillna(0).clip(lower=0)
    df["gross_sales"] = df["quantity"] * df["unit_price"]
    df["revenue"] = (df["gross_sales"] - df["discount"]).clip(lower=0)
    df["month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()
    cleaning = {
        "original_rows": original_rows,
        "duplicates_removed": original_rows - after_duplicates,
        "invalid_or_incomplete_rows_removed": after_duplicates - len(df),
        "clean_rows": len(df),
    }
    if df.empty:
        raise ValueError("No valid records remain after cleaning. Check the CSV data.")
    return df, cleaning

def create_visualizations(df: pd.DataFrame) -> dict:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("ggplot")
    paths = {}

    category_sales = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(category_sales.index, category_sales.values)
    ax.set_title("Revenue by Product Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Revenue (INR)")
    ax.bar_label(bars, fmt="₹%.0f", padding=3)
    fig.tight_layout()
    paths["category"] = CHART_DIR / "revenue_by_category.png"
    fig.savefig(paths["category"], dpi=160, bbox_inches="tight")
    plt.close(fig)

    monthly_sales = df.groupby("month")["revenue"].sum().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_sales.index, monthly_sales.values, marker="o", linewidth=2)
    ax.set_title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (INR)")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    paths["monthly"] = CHART_DIR / "monthly_revenue_trend.png"
    fig.savefig(paths["monthly"], dpi=160, bbox_inches="tight")
    plt.close(fig)

    city_sales = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(city_sales.values, labels=city_sales.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Revenue Share by City", fontsize=14, fontweight="bold")
    fig.tight_layout()
    paths["city"] = CHART_DIR / "revenue_share_by_city.png"
    fig.savefig(paths["city"], dpi=160, bbox_inches="tight")
    plt.close(fig)
    return paths

def build_report(df: pd.DataFrame, cleaning: dict, paths: dict) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    total_revenue = df["revenue"].sum()
    total_units = int(df["quantity"].sum())
    average_order_revenue = df["revenue"].mean()
    category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    monthly = df.groupby("month")["revenue"].sum().sort_index()
    cities = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
    best_category, best_category_value = category.index[0], category.iloc[0]
    best_month, best_month_value = monthly.idxmax(), monthly.max()
    best_city, best_city_value = cities.index[0], cities.iloc[0]
    weakest_month, weakest_month_value = monthly.idxmin(), monthly.min()

    lines = [
        "# E-commerce Sales Analysis Report", "",
        "> **Dataset note:** This is a sample learning dataset, not real business data.", "",
        "## 1. Executive Summary", "",
        f"- **Total revenue:** ₹{total_revenue:,.2f}",
        f"- **Units sold:** {total_units:,}",
        f"- **Valid order records:** {len(df):,}",
        f"- **Average revenue per record:** ₹{average_order_revenue:,.2f}",
        f"- **Top category:** {best_category} (₹{best_category_value:,.2f})",
        f"- **Top city:** {best_city} (₹{best_city_value:,.2f})", "",
        "## 2. Data Quality", "",
        f"- Rows loaded: {cleaning['original_rows']}",
        f"- Duplicate rows removed: {cleaning['duplicates_removed']}",
        f"- Invalid/incomplete rows removed: {cleaning['invalid_or_incomplete_rows_removed']}",
        f"- Rows retained: {cleaning['clean_rows']}", "",
        "## 3. Key Findings", "",
        f"1. **Category performance:** {best_category} generated the highest revenue at ₹{best_category_value:,.2f}.",
        f"2. **Monthly trend:** {best_month.strftime('%B %Y')} was the strongest month (₹{best_month_value:,.2f}); {weakest_month.strftime('%B %Y')} was the weakest (₹{weakest_month_value:,.2f}).",
        f"3. **City performance:** {best_city} contributed the most revenue at ₹{best_city_value:,.2f}, approximately {best_city_value / total_revenue * 100:.1f}% of total revenue.",
        "4. **Business interpretation:** Revenue differences may reflect order volume, product mix, and discounts. More data would be needed before treating these patterns as long-term trends.", "",
        "## 4. Visualizations", "",
        "### Revenue by Product Category", "",
        "![Revenue by category](../visualizations/revenue_by_category.png)", "",
        "### Monthly Revenue Trend", "",
        "![Monthly revenue trend](../visualizations/monthly_revenue_trend.png)", "",
        "### Revenue Share by City", "",
        "![Revenue share by city](../visualizations/revenue_share_by_city.png)", "",
        "## 5. Revenue by Category", "",
        "| Category | Revenue |",
        "|---|---:|",
    ]
    for name, value in category.items():
        lines.append(f"| {name} | ₹{value:,.2f} |")
    lines += ["", "## 6. Recommendations", "",
        f"- Review the product mix and stock availability in the **{best_category}** category to understand what is driving its performance.",
        f"- Investigate the causes of the revenue dip in **{weakest_month.strftime('%B %Y')}** before changing budgets or inventory.",
        f"- Compare marketing spend and order counts by city, especially in **{best_city}**, before reallocating campaigns.",
        "- Continue collecting consistent data over multiple periods; avoid drawing conclusions from this sample alone.", "",
        "## 7. Methodology", "",
        "1. Loaded the CSV dataset with pandas.",
        "2. Parsed dates and converted numeric columns.",
        "3. Removed duplicate rows and records missing essential fields; excluded non-positive quantities.",
        "4. Calculated revenue as `(quantity × unit_price) - discount`.",
        "5. Aggregated revenue by category, month, and city.",
        "6. Generated charts using Matplotlib and wrote this report.", "",
        "## 8. Limitations", "",
        "- The dataset is synthetic and intentionally small for practice.",
        "- Discount is treated as a fixed amount per row, not a per-unit discount.",
        "- No costs or returns are provided, so this report analyzes revenue rather than profit.", ""
    ]
    report_path = REPORT_DIR / "analysis_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path

def main() -> int:
    try:
        df, cleaning = load_and_clean_data(DATA_FILE)
        paths = create_visualizations(df)
        report_path = build_report(df, cleaning, paths)
        print("Analysis completed successfully.")
        print(f"Rows retained: {cleaning['clean_rows']} / {cleaning['original_rows']}")
        print(f"Total revenue: ₹{df['revenue'].sum():,.2f}")
        print(f"Charts saved to: {CHART_DIR}")
        print(f"Report saved to: {report_path}")
        return 0
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
