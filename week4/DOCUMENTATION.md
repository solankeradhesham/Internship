# Project Documentation: E-commerce Sales Analysis

## Objective
Analyze a sample e-commerce dataset to understand revenue by product category, month, and city. The project demonstrates a complete beginner-level data workflow: loading, cleaning, analysis, visualization, and reporting.

## Tools
- Python
- pandas for data loading and aggregation
- Matplotlib for charts
- CSV for source data
- Markdown for the final report

## Data fields
| Field | Description |
|---|---|
| `order_date` | Date of the order record |
| `category` | Product category |
| `product` | Product name |
| `city` | City associated with the sale |
| `quantity` | Units sold |
| `unit_price` | Price per unit in INR |
| `discount` | Discount amount for the row in INR |

## Workflow
1. Read `data/sales_data.csv`.
2. Validate required columns and convert dates/numbers.
3. Remove duplicate records and rows missing essential data.
4. Calculate gross sales and revenue after discount.
5. Aggregate revenue by category, month, and city.
6. Save a bar chart, line chart, and pie chart to `visualizations/`.
7. Generate `report/analysis_report.md` with numerical results and written insights.

## Charts
- `revenue_by_category.png`: compares revenue across categories.
- `monthly_revenue_trend.png`: shows changes in revenue over time.
- `revenue_share_by_city.png`: shows each city's share of revenue.

## Error handling
The program checks whether the CSV exists, verifies required columns, rejects an empty cleaned dataset, parses invalid values safely, and prints a readable error message when analysis cannot proceed.

## Limitations
The included dataset is synthetic and small. Discounts are modeled as fixed row-level amounts. Costs, refunds, and profit are not included, so conclusions should be about revenue only.

## How to run
Install dependencies using `python -m pip install -r requirements.txt`, then run `python main.py`. The charts and report will be generated or refreshed.
