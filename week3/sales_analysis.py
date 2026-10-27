"""
Week 3 Project: Sales Data Analysis
Loads a CSV, cleans missing/duplicate records, calculates metrics, and writes a Markdown report.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
REPORT_FILE = BASE_DIR / "analysis_report.md"


def load_and_clean_data(file_path: Path) -> tuple[pd.DataFrame, dict]:
    """Load sales data and apply simple, documented cleaning rules."""
    df = pd.read_csv(file_path)
    original_rows = len(df)

    # Remove exact duplicate records before calculating metrics.
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Convert numeric fields safely; invalid values become missing values.
    for column in ["Quantity", "Unit_Price", "Total_Sales"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Rows without a product name cannot be grouped meaningfully, so remove them.
    missing_product_rows = int(df["Product"].isna().sum())
    df = df.dropna(subset=["Product"]).copy()

    # Fill missing quantities with 0, as missing quantity is treated as no units sold.
    # For missing prices/sales, calculate Total_Sales from Quantity × Unit_Price when possible.
    missing_quantity_count = int(df["Quantity"].isna().sum())
    df["Quantity"] = df["Quantity"].fillna(0)

    calculated_sales = df["Quantity"] * df["Unit_Price"]
    df["Total_Sales"] = df["Total_Sales"].fillna(calculated_sales)

    # Keep only rows with a usable sales amount after attempted calculation.
    missing_sales_count = int(df["Total_Sales"].isna().sum())
    df = df.dropna(subset=["Total_Sales"]).copy()

    cleaning_summary = {
        "original_rows": original_rows,
        "duplicate_rows_removed": duplicate_count,
        "rows_without_product_removed": missing_product_rows,
        "missing_quantities_filled": missing_quantity_count,
        "unresolved_sales_rows_removed": missing_sales_count,
        "cleaned_rows": len(df),
    }
    return df, cleaning_summary


def build_report(df: pd.DataFrame, cleaning: dict) -> str:
    """Create a clear Markdown report from the cleaned data."""
    total_revenue = float(df["Total_Sales"].sum())
    total_units = int(df["Quantity"].sum())
    average_order_value = float(df["Total_Sales"].mean())
    highest_sale = float(df["Total_Sales"].max())
    lowest_sale = float(df["Total_Sales"].min())

    product_revenue = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    best_product = str(product_revenue.index[0])
    best_product_revenue = float(product_revenue.iloc[0])

    region_revenue = df.groupby("Region", dropna=False)["Total_Sales"].sum().sort_values(ascending=False)
    top_region = str(region_revenue.index[0])
    top_region_revenue = float(region_revenue.iloc[0])

    product_lines = "\n".join(
        f"| {product} | ₹{revenue:,.2f} |"
        for product, revenue in product_revenue.items()
    )

    return f"""# Sales Data Analysis Report

## Overview
This report analyzes the supplied sample sales dataset after basic data cleaning.

## Data cleaning summary
- Rows before cleaning: {cleaning['original_rows']}
- Duplicate rows removed: {cleaning['duplicate_rows_removed']}
- Rows without product names removed: {cleaning['rows_without_product_removed']}
- Missing quantities filled with 0: {cleaning['missing_quantities_filled']}
- Rows with unresolved sales values removed: {cleaning['unresolved_sales_rows_removed']}
- Rows used for analysis: {cleaning['cleaned_rows']}

## Key metrics
- **Total revenue:** ₹{total_revenue:,.2f}
- **Total units sold:** {total_units:,}
- **Average sale value:** ₹{average_order_value:,.2f}
- **Highest single sale:** ₹{highest_sale:,.2f}
- **Lowest single sale:** ₹{lowest_sale:,.2f}
- **Best-selling product by revenue:** {best_product} (₹{best_product_revenue:,.2f})
- **Top region by revenue:** {top_region} (₹{top_region_revenue:,.2f})

## Revenue by product
| Product | Revenue |
|---|---:|
{product_lines}

## Insights
1. **{best_product}** generated the highest revenue in this sample.
2. Total revenue across the cleaned records was **₹{total_revenue:,.2f}**.
3. The dataset contains {cleaning['cleaned_rows']} usable sales records after cleaning.

## Notes and assumptions
- This is an illustrative practice dataset, not real business data.
- Missing quantities are treated as zero units.
- If a sales amount is missing, it is calculated from quantity multiplied by unit price when possible.
- Records without a product name are excluded because they cannot be assigned to a product.
- Revenue is calculated from the `Total_Sales` column after the cleaning steps above.
"""


def main() -> None:
    # Load and clean the dataset.
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE.name}. Keep it beside this script.")

    sales_df, cleaning_summary = load_and_clean_data(DATA_FILE)

    # Print a quick overview so users can inspect the data in the terminal.
    print("\n--- Cleaned sales data (first 5 rows) ---")
    print(sales_df.head().to_string(index=False))
    print("\n--- Dataset information ---")
    print(f"Rows: {len(sales_df)}")
    print(f"Columns: {', '.join(sales_df.columns)}")
    print("\n--- Missing values after cleaning ---")
    print(sales_df.isna().sum().to_string())

    # Generate and save the formatted Markdown report.
    report = build_report(sales_df, cleaning_summary)
    REPORT_FILE.write_text(report, encoding="utf-8")

    print("\n--- Key metrics ---")
    print(f"Total revenue: ₹{sales_df['Total_Sales'].sum():,.2f}")
    print(f"Best-selling product by revenue: {sales_df.groupby('Product')['Total_Sales'].sum().idxmax()}")
    print(f"Report saved to: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
