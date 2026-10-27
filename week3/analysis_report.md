# Sales Data Analysis Report

## Overview
This report analyzes the supplied sample sales dataset after basic data cleaning.

## Data cleaning summary
- Rows before cleaning: 16
- Duplicate rows removed: 1
- Rows without product names removed: 1
- Missing quantities filled with 0: 1
- Rows with unresolved sales values removed: 0
- Rows used for analysis: 14

## Key metrics
- **Total revenue:** ₹12,700.00
- **Total units sold:** 147
- **Average sale value:** ₹907.14
- **Highest single sale:** ₹3,200.00
- **Lowest single sale:** ₹0.00
- **Best-selling product by revenue:** Backpack (₹7,200.00)
- **Top region by revenue:** South (₹7,200.00)

## Revenue by product
| Product | Revenue |
|---|---:|
| Backpack | ₹7,200.00 |
| Water Bottle | ₹2,750.00 |
| Notebook | ₹1,850.00 |
| Pen | ₹900.00 |

## Insights
1. **Backpack** generated the highest revenue in this sample.
2. Total revenue across the cleaned records was **₹12,700.00**.
3. The dataset contains 14 usable sales records after cleaning.

## Notes and assumptions
- This is an illustrative practice dataset, not real business data.
- Missing quantities are treated as zero units.
- If a sales amount is missing, it is calculated from quantity multiplied by unit price when possible.
- Records without a product name are excluded because they cannot be assigned to a product.
- Revenue is calculated from the `Total_Sales` column after the cleaning steps above.
