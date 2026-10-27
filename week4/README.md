# Week 4: E-commerce Sales Analysis

A beginner-friendly end-to-end Python data analysis project using **pandas** and **Matplotlib**.

## Features
- Loads and validates a CSV dataset.
- Cleans duplicate and incomplete records.
- Calculates revenue, units sold, category performance, monthly trends, and city contribution.
- Creates a bar chart, line chart, and pie chart.
- Generates a written report with metrics, findings, recommendations, and embedded charts.
- Includes error handling for missing files, missing columns, and invalid data.

> The included dataset is synthetic sample data for learning. Do not present it as real company data.

## Project structure
```text
week-4-ecommerce-sales-analysis/
├── main.py
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
├── data/
│   └── sales_data.csv
├── visualizations/
│   ├── revenue_by_category.png
│   ├── monthly_revenue_trend.png
│   └── revenue_share_by_city.png
└── report/
    └── analysis_report.md
```

## Run locally

Python 3.10+ recommended.

### 1. Open a terminal in this project folder
```bash
cd week-4-ecommerce-sales-analysis
```

### 2. Create and activate a virtual environment (recommended)
Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Run the analysis
```bash
python main.py
```

The script updates the charts in `visualizations/` and the report in `report/analysis_report.md`.

## How revenue is calculated
`revenue = (quantity × unit_price) - discount`

Revenue is not the same as profit because the dataset does not include costs.

## Customize the project
Replace `data/sales_data.csv` with your own dataset, keeping the required column names:
`order_date, category, product, city, quantity, unit_price, discount`

After changing the data, run `python main.py` again.

## GitHub submission checklist
- [ ] Upload the complete project folder to your Week 4 repository folder.
- [ ] Keep `data/`, `visualizations/`, and `report/` in the repository.
- [ ] Open `report/analysis_report.md` and review the findings.
- [ ] Run `python main.py` successfully on your own computer.
- [ ] Add your own screenshots if your instructor asks for them.
