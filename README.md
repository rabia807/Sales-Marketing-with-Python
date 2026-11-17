# Sales Marketing with Python

A beginner-friendly data analytics project that explores sales results and marketing campaign performance with **Python, pandas, and Matplotlib**.

> **Dataset note:** The included CSV contains illustrative, synthetic sample data created for learning and demonstration. It is not real customer or company data.

## Project objectives

- Calculate revenue and marketing spend.
- Review product and regional sales performance.
- Measure leads, conversions, and visit-to-conversion rate.
- Compare marketing campaigns using Return on Ad Spend (ROAS).
- Generate charts to make trends easier to understand.

## Repository structure

```text
Sales-Marketing-with-Python/
├── data/
│   └── sales_marketing_data.csv
├── outputs/                     # Generated charts (created when script runs)
├── sales_marketing_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Tools and libraries

- Python 3.9+
- pandas — data cleaning, grouping, and calculations
- Matplotlib — charts and visualizations

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

4. Run the analysis:

   ```bash
   python sales_marketing_analysis.py
   ```

The script prints a performance summary in the terminal and creates three PNG charts inside the `outputs/` folder.

## Metrics explained

| Metric | Meaning |
|---|---|
| Revenue | Units sold multiplied by unit price |
| Marketing spend | Amount spent on the campaign |
| ROAS | Revenue divided by marketing spend |
| Conversion rate | Conversions divided by website visits, multiplied by 100 |
| Revenue after ad spend | Revenue minus marketing spend; not the same as net profit |

**Important:** ROAS is a revenue-to-ad-spend ratio. It does not account for product costs, salaries, taxes, or other operating expenses, so it should not be interpreted as net profit.

## Generated visualizations

- `outputs/monthly_revenue.png` — monthly revenue trend
- `outputs/revenue_by_product.png` — revenue comparison by product
- `outputs/campaign_roas.png` — campaign ROAS comparison

## Ideas to extend the project

- Add more months and regions.
- Import your own anonymized sales CSV.
- Compare campaign conversion rates and cost per lead.
- Build an interactive dashboard with Streamlit.
- Add unit tests and automated data-quality checks.

## Author

Created as a portfolio learning project for sales and marketing analytics.
