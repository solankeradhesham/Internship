# Week 3: Introduction to Data Analysis — Sales Data Analysis

This beginner-friendly project uses pandas to clean and analyze a small sample sales CSV and generate a Markdown report.

## Files
- `sales_analysis.py` — loads, cleans, analyzes, and reports on the data
- `sales_data.csv` — sample dataset with a few missing values and a duplicate row for practice
- `analysis_report.md` — generated analysis report
- `requirements.txt` — Python dependency

## Setup
Python 3.10+ is recommended.

```bash
python -m pip install -r requirements.txt
```

On Windows, if `python` is not recognized, try:

```powershell
py -m pip install -r requirements.txt
```

## Run
Keep the CSV beside the Python script, then run:

```bash
python sales_analysis.py
```

On Windows, you can also use `py sales_analysis.py`.

The script prints an overview and saves/updates `analysis_report.md`.

## Cleaning rules
- Remove exact duplicate rows.
- Remove records without a product name.
- Convert numeric columns to numeric values.
- Fill missing quantities with 0.
- Calculate missing sales values using quantity × unit price where possible.
- Exclude rows that still have no usable sales amount.

These are teaching assumptions for the sample dataset. Real projects should confirm data-cleaning decisions with the data owner.

## Metrics
The report includes total revenue, total units sold, average sale value, highest and lowest sale, best product by revenue, and revenue by product.

## Submission
Run the script, review the generated `analysis_report.md`, and push all required files to GitHub.
