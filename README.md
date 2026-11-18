# Sales Marketing with Python

A beginner-friendly data analytics project that explores sales results and marketing campaign performance with **Python, pandas, Matplotlib, and Streamlit**.

> **Dataset note:** The included CSV contains illustrative, synthetic sample data created for learning and demonstration. It is not real customer or company data.

## Project objectives

- Calculate revenue and marketing spend.
- Review product and regional sales performance.
- Measure leads, conversions, and visit-to-conversion rate.
- Compare marketing campaigns using Return on Ad Spend (ROAS).
- Generate charts and explore results in an interactive dashboard.

## Repository structure

```text
Sales-Marketing-with-Python/
├── data/
│   └── sales_marketing_data.csv
├── outputs/                     # Static charts created by analysis script
├── sales_marketing_analysis.py
├── streamlit_app.py              # Interactive dashboard
├── requirements.txt
├── .gitignore
└── README.md
```

## Tools and libraries

- Python 3.9+
- pandas — data cleaning, grouping, and calculations
- Matplotlib — static charts
- Streamlit — interactive dashboard

## Getting started

1. Clone this repository:

   ```bash
   git clone https://github.com/rabia807/Sales-Marketing-with-Python.git
   cd Sales-Marketing-with-Python
   ```

2. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Python analysis

```bash
python sales_marketing_analysis.py
```

The script prints a performance summary and creates three PNG charts inside the `outputs/` folder.

## Launch the interactive dashboard

```bash
streamlit run streamlit_app.py
```

Streamlit will open the dashboard in your browser. Use the sidebar to filter by date, region, product, and campaign. The dashboard includes:

- KPI cards for revenue, marketing spend, ROAS, units sold, and conversion rate
- Monthly revenue trend
- Revenue by product and region
- Campaign performance table
- Filtered sales data with CSV download

## Metrics explained

| Metric | Meaning |
|---|---|
| Revenue | Units sold multiplied by unit price |
| Marketing spend | Amount spent on the campaign |
| ROAS | Revenue divided by marketing spend |
| Conversion rate | Conversions divided by website visits, multiplied by 100 |
| Revenue after ad spend | Revenue minus marketing spend; not the same as net profit |

**Important:** ROAS is a revenue-to-ad-spend ratio. It does not account for product costs, salaries, taxes, or other operating expenses, so it should not be interpreted as net profit.

## Ideas to extend the project

- Add more months and regions.
- Import your own anonymized sales CSV.
- Compare campaign conversion rates and cost per lead.
- Deploy the Streamlit dashboard using Streamlit Community Cloud.
- Add unit tests and automated data-quality checks.

## Author

Created as a portfolio learning project for sales and marketing analytics.
