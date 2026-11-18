"""Interactive Streamlit dashboard for the Sales Marketing with Python project."""
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "sales_marketing_data.csv"

st.set_page_config(page_title="Sales & Marketing Dashboard", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    df["revenue"] = df["units_sold"] * df["unit_price"]
    df["conversion_rate_pct"] = (
        df["conversions"] / df["website_visits"].replace(0, pd.NA) * 100
    ).fillna(0)
    return df

st.title("📊 Sales & Marketing Performance Dashboard")
st.caption("Explore sales trends, product performance, and marketing campaign results. Sample dataset for demonstration.")

df = load_data()

with st.sidebar:
    st.header("Dashboard filters")
    regions = st.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
    products = st.multiselect("Product", sorted(df["product"].unique()), default=sorted(df["product"].unique()))
    campaigns = st.multiselect("Campaign", sorted(df["campaign"].unique()), default=sorted(df["campaign"].unique()))
    min_date, max_date = df["date"].min().date(), df["date"].max().date()
    date_range = st.date_input("Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

filtered = df[
    df["region"].isin(regions)
    & df["product"].isin(products)
    & df["campaign"].isin(campaigns)
].copy()

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["date"].dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.warning("No records match these filters. Please widen your selection.")
    st.stop()

revenue = filtered["revenue"].sum()
spend = filtered["marketing_spend"].sum()
units = filtered["units_sold"].sum()
visits = filtered["website_visits"].sum()
conversions = filtered["conversions"].sum()
roas = revenue / spend if spend else 0
conversion_rate = conversions / visits * 100 if visits else 0

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total revenue", f"${revenue:,.0f}")
k2.metric("Marketing spend", f"${spend:,.0f}")
k3.metric("ROAS", f"{roas:.2f}x")
k4.metric("Units sold", f"{units:,.0f}")
k5.metric("Conversion rate", f"{conversion_rate:.2f}%")

st.divider()
left, right = st.columns(2)

with left:
    st.subheader("Monthly revenue")
    monthly = filtered.set_index("date").resample("MS")["revenue"].sum()
    st.line_chart(monthly, use_container_width=True)

with right:
    st.subheader("Revenue by product")
    product_revenue = filtered.groupby("product")["revenue"].sum().sort_values(ascending=False)
    st.bar_chart(product_revenue, horizontal=True, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Campaign performance")
    campaign = filtered.groupby("campaign").agg(
        Revenue=("revenue", "sum"),
        Spend=("marketing_spend", "sum"),
        Conversions=("conversions", "sum"),
    )
    campaign["ROAS"] = (campaign["Revenue"] / campaign["Spend"].replace(0, pd.NA)).round(2)
    st.dataframe(campaign.sort_values("ROAS", ascending=False), use_container_width=True)

with right:
    st.subheader("Revenue by region")
    region_revenue = filtered.groupby("region")["revenue"].sum().sort_values(ascending=False)
    st.bar_chart(region_revenue, use_container_width=True)

st.subheader("Filtered sales data")
display_columns = ["date", "region", "product", "units_sold", "unit_price", "revenue",
                   "marketing_spend", "website_visits", "leads", "conversions", "campaign"]
st.dataframe(filtered[display_columns].sort_values("date", ascending=False), use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download filtered data (CSV)", data=csv,
                   file_name="filtered_sales_marketing_data.csv", mime="text/csv")

st.caption("ROAS = revenue ÷ marketing spend. It is not net profit; product costs and operating expenses are not included.")
