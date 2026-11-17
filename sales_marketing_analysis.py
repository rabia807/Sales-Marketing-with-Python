"""Sales and marketing performance analysis using pandas and matplotlib."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "sales_marketing_data.csv"
OUTPUT_DIR = ROOT / "outputs"

def load_data() -> pd.DataFrame:
    """Load the sample dataset and prepare calculated columns."""
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    numeric = ["units_sold", "unit_price", "marketing_spend", "website_visits", "leads", "conversions"]
    df[numeric] = df[numeric].apply(pd.to_numeric, errors="coerce")
    df = df.dropna(subset=numeric + ["date", "region", "product", "campaign"])
    df = df[(df["units_sold"] >= 0) & (df["unit_price"] >= 0)]
    df["revenue"] = df["units_sold"] * df["unit_price"]
    df["conversion_rate_pct"] = (df["conversions"] / df["website_visits"].replace(0, pd.NA) * 100).fillna(0)
    df["roas"] = df["revenue"] / df["marketing_spend"].replace(0, pd.NA)
    return df

def print_summary(df: pd.DataFrame) -> None:
    total_revenue = df["revenue"].sum()
    total_spend = df["marketing_spend"].sum()
    total_conversions = df["conversions"].sum()
    overall_roas = total_revenue / total_spend if total_spend else 0
    visits = df["website_visits"].sum()
    conversion_rate = total_conversions / visits * 100 if visits else 0

    print("\n=== SALES & MARKETING OVERVIEW ===")
    print(f"Rows analysed: {len(df):,}")
    print(f"Total revenue: $" + f"{total_revenue:,.2f}")
    print(f"Marketing spend: $" + f"{total_spend:,.2f}")
    print(f"Revenue after ad spend: $" + f"{total_revenue-total_spend:,.2f}")
    print(f"Return on ad spend (ROAS): {overall_roas:.2f}x")
    print(f"Website visits: {visits:,}")
    print(f"Leads: {df['leads'].sum():,}")
    print(f"Conversions: {total_conversions:,}")
    print(f"Visit-to-conversion rate: {conversion_rate:.2f}%")

    print("\nRevenue by product:")
    print(df.groupby("product")["revenue"].sum().sort_values(ascending=False).round(2))
    print("\nCampaign performance:")
    campaign = df.groupby("campaign").agg(revenue=("revenue", "sum"), spend=("marketing_spend", "sum"), conversions=("conversions", "sum"))
    campaign["roas"] = campaign["revenue"] / campaign["spend"].replace(0, pd.NA)
    print(campaign.sort_values("roas", ascending=False).round(2))

def create_charts(df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    monthly = df.set_index("date").resample("MS")["revenue"].sum()
    product_revenue = df.groupby("product")["revenue"].sum().sort_values()
    campaign = df.groupby("campaign").agg(revenue=("revenue", "sum"), spend=("marketing_spend", "sum"))
    campaign["roas"] = campaign["revenue"] / campaign["spend"].replace(0, pd.NA)

    fig, ax = plt.subplots(figsize=(9, 5))
    monthly.plot(marker="o", ax=ax)
    ax.set(title="Monthly Revenue", xlabel="Month", ylabel="Revenue ($)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    product_revenue.plot(kind="barh", ax=ax)
    ax.set(title="Revenue by Product", xlabel="Revenue ($)", ylabel="Product")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "revenue_by_product.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    campaign["roas"].sort_values().plot(kind="barh", ax=ax)
    ax.set(title="Return on Ad Spend by Campaign", xlabel="ROAS (x)", ylabel="Campaign")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "campaign_roas.png", dpi=150)
    plt.close(fig)
    print(f"\nCharts saved in: {OUTPUT_DIR}")

def main() -> None:
    df = load_data()
    if df.empty:
        raise ValueError("The dataset contains no valid rows.")
    print_summary(df)
    create_charts(df)

if __name__ == "__main__":
    main()
