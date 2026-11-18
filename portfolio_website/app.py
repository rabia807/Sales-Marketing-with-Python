import streamlit as st

st.set_page_config(page_title="Rabia Bashir | Data Analyst", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:'DM Sans',sans-serif;}
.stApp {background:linear-gradient(180deg,#f8f8ff 0%,#fff 55%,#f7f9ff 100%);}
.block-container {max-width:1120px;padding-top:2rem;padding-bottom:3rem;}
.hero {padding:3rem 2.5rem;border-radius:26px;background:linear-gradient(120deg,#17213d,#38336f 60%,#6d5dfc);color:white;}
.hero h1 {font-family:Manrope,sans-serif;color:white;font-size:clamp(2.3rem,5vw,4rem);line-height:1.08;}
.hero p {color:#e6e7ff;font-size:1.05rem;max-width:700px;}
.kicker {color:#c9c8ff;text-transform:uppercase;letter-spacing:.15em;font-size:.75rem;font-weight:700;}
.card {background:white;border:1px solid #e8e9f3;border-radius:18px;padding:1.25rem;height:100%;box-shadow:0 8px 28px #20264a08;}
.card h3 {font-family:Manrope,sans-serif;font-size:1.05rem;}
.muted {color:#64748b;line-height:1.65;}
.tag {display:inline-block;background:#f0efff;color:#5143c5;padding:.35rem .65rem;border-radius:8px;margin:.18rem;font-size:.82rem;}
.project {background:#f5f4ff;border:1px solid #e5e2ff;border-radius:18px;padding:1.4rem;}
div.stButton>button {border-radius:999px;background:#6d5dfc;color:white;border:0;font-weight:700;}
</style>
""", unsafe_allow_html=True)

FIVERR = "https://www.fiverr.com/rabia807"
GITHUB = "https://github.com/rabia807/Sales-Marketing-with-Python"
AVATAR = "https://fiverr-res.cloudinary.com/image/upload/f_auto,q_auto,t_profile_original/v1/attachments/profile/photo/c2e1e79c42211c3a7854ebf692436c23-1793888101660/f91b46b2-316f-45ea-8ab0-ebff6edccc76.png"

a,b,c = st.columns([3,1,1])
with a: st.markdown("### **RB.**  <span style='color:#6d5dfc'>Rabia Bashir</span>", unsafe_allow_html=True)
with b: st.markdown("[Services](#services)")
with c: st.markdown("[Contact](#contact)")

st.markdown("""
<div class="hero">
<div class="kicker">Statistician · Data Analyst · Research Support</div>
<h1>Turning complex data<br>into clear decisions.</h1>
<p>I'm Rabia Bashir, an MPhil Statistician and Data Analyst. I help transform datasets into clear insights through statistical analysis, research-ready reporting, dashboards and forecasting.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
x,y = st.columns([1,2],gap="large")
with x: st.image(AVATAR,width=185)
with y:
    st.markdown('<div class="kicker" style="color:#6d5dfc">About me</div>',unsafe_allow_html=True)
    st.header("Hello, I'm Rabia.")
    st.markdown('<p class="muted">My Fiverr profile describes 5+ years of freelancing experience. I work with statistical analysis, data cleaning, quantitative research and dashboard reporting. I communicate in English and Urdu, and value clear explanations and careful handling of client data.</p>',unsafe_allow_html=True)

st.markdown('<div id="services"></div><div class="kicker" style="color:#6d5dfc">What I do</div>',unsafe_allow_html=True)
st.header("Services")
services=[
("📊","Statistical analysis","Descriptive statistics, hypothesis testing, t-tests, ANOVA, chi-square, correlation and regression."),
("🧹","Data cleaning","Organizing datasets, handling missing values and preparing data for analysis."),
("📈","Dashboards & reporting","Power BI, Excel and Google Sheets dashboards with clear visual summaries."),
("🔬","Research & forecasting","Quantitative research support, time-series analysis, forecasting and interpretation.")
]
cols=st.columns(4)
for col,(ico,title,desc) in zip(cols,services):
    with col: st.markdown(f'<div class="card"><div style="font-size:1.7rem">{ico}</div><h3>{title}</h3><div class="muted">{desc}</div></div>',unsafe_allow_html=True)

st.write("")
st.markdown('<div class="kicker" style="color:#6d5dfc">Tools & technologies</div>',unsafe_allow_html=True)
st.header("My toolkit")
st.markdown("".join(f'<span class="tag">{t}</span>' for t in ["Python","Pandas","Matplotlib","SPSS","R / RStudio","Power BI","Excel","Google Sheets","Minitab"]),unsafe_allow_html=True)

st.write("")
st.markdown('<div class="kicker" style="color:#6d5dfc">Selected work</div>',unsafe_allow_html=True)
st.header("Project")
st.markdown("""
<div class="project">
<div class="kicker" style="color:#6d5dfc">Python · Pandas · Matplotlib · Streamlit</div>
<h3>Sales Marketing Analysis Dashboard</h3>
<p class="muted">An illustrative portfolio project exploring revenue, marketing spend, ROAS, units sold, conversion rate, product performance, regional sales and campaign results through an interactive dashboard.</p>
<span class="tag">Data Analysis</span><span class="tag">KPI Dashboard</span><span class="tag">Visualization</span>
</div>
""",unsafe_allow_html=True)
st.link_button("View project on GitHub ↗",GITHUB)

st.write("")
st.markdown('<div id="contact"></div><div class="kicker" style="color:#6d5dfc">Let's work together</div>',unsafe_allow_html=True)
st.header("Have a data project in mind?")
st.markdown('<p class="muted">Message me on Fiverr to discuss your dataset, research question or dashboard requirements. Please share your goals and relevant details before ordering.</p>',unsafe_allow_html=True)
st.link_button("Contact Rabia on Fiverr ↗",FIVERR)
st.divider()
st.caption("© 2026 Rabia Bashir · Data Analysis & Statistical Consulting")
st.caption("The Sales Marketing demo uses illustrative sample data, not real client or company data.")
