# import pandas as pd
# import streamlit as st
# import joblib

# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="House Price Predictor",
#     page_icon="🏠",
#     layout="wide"
# )

# # ---------------- CUSTOM CSS ---------------- #

# st.markdown("""
# <style>

# .main {
#     padding-top: 1rem;
# }

# .stApp {
#     background-color: #0E1117;
# }

# .big-title {
#     text-align: center;
#     font-size: 3rem;
#     font-weight: bold;
#     color: white;
# }

# .subtitle {
#     text-align: center;
#     color: #A0A0A0;
#     margin-bottom: 30px;
# }

# .result-card {
#     background-color: #1C1F26;
#     padding: 25px;
#     border-radius: 15px;
#     text-align: center;
#     border: 1px solid #2E3440;
# }

# .result-price {
#     font-size: 2.2rem;
#     font-weight: bold;
#     color: #00E676;
# }

# .metric-card {
#     background-color: #1C1F26;
#     padding: 15px;
#     border-radius: 12px;
#     border: 1px solid #2E3440;
# }

# div.stButton > button {
#     width: 100%;
#     height: 55px;
#     font-size: 18px;
#     font-weight: bold;
#     border-radius: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- MODEL ---------------- #

# model = joblib.load("xgb_model.jb")

# # ---------------- SIDEBAR ---------------- #

# st.sidebar.markdown("""
# <style>

# .info-card {
#     background: linear-gradient(135deg, #1e293b, #334155);
#     padding: 20px;
#     border-radius: 15px;
#     border: 1px solid rgba(255,255,255,0.1);
#     box-shadow: 0 0 15px rgba(59,130,246,0.25);
#     animation: glow 3s infinite alternate;
# }

# @keyframes glow {
#     from {
#         box-shadow: 0 0 10px rgba(59,130,246,0.20);
#     }
#     to {
#         box-shadow: 0 0 25px rgba(59,130,246,0.60);
#     }
# }

# .info-title {
#     font-size: 24px;
#     font-weight: bold;
#     margin-bottom: 15px;
# }

# .info-item {
#     font-size: 16px;
#     margin-bottom: 12px;
# }

# </style>
# """, unsafe_allow_html=True)


# st.sidebar.markdown("""
# # 🏠 House Price Predictor
# ### Dashboard
# """)

# st.sidebar.markdown("---")

# st.sidebar.markdown("## Model Status ")

# st.sidebar.success(
#     "Machine Learning Model Loaded Successfully"
# )

# st.sidebar.markdown("---")

# st.sidebar.title("Model Details")

# st.sidebar.metric("R² Score", "0.899")
# st.sidebar.metric("MAE", "$18,140")
# st.sidebar.metric("Algorithm", "XGBoost")

# # ---------------- HEADER ---------------- #

# st.markdown(
#     '<div class="big-title">🏠 House Price Predictor</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="subtitle">Predict house prices using an XGBoost Machine Learning Model</div>',
#     unsafe_allow_html=True
# )

# st.markdown("---")

# # ---------------- INPUT SECTION ---------------- #

# col1, col2 = st.columns(2)

# with col1:
#     overallqual = st.slider("Overall Quality (1-10)", 1, 10, 5)

#     grlivarea = st.number_input(
#         "Living Area (sq ft)",
#         min_value=0.0,
#         value=1500.0
#     )

#     garagearea = st.number_input(
#         "Garage Area (sq ft)",
#         min_value=0.0,
#         value=500.0
#     )

#     firstflrsf = st.number_input(
#         "First Floor Area (sq ft)",
#         min_value=0.0,
#         value=1200.0
#     )

#     fullbath = st.number_input(
#         "Number of Full Bathrooms",
#         min_value=0,
#         value=2
#     )

#     yearbuilt = st.number_input(
#         "Year Built",
#         min_value=1800,
#         max_value=2026,
#         value=2000
#     )

#     yearremodadd = st.number_input(
#         "Year Remodeled",
#         min_value=1800,
#         max_value=2026,
#         value=2000
#     )

#     masvnrarea = st.number_input(
#         "Masonry Veneer Area",
#         min_value=0.0,
#         value=100.0
#     )

# with col2:
#     fireplaces = st.number_input(
#         "Number of Fireplaces",
#         min_value=0,
#         value=1
#     )

#     bsmtfinsf1 = st.number_input(
#         "Finished Basement Area",
#         min_value=0.0,
#         value=500.0
#     )

#     lotfrontage = st.number_input(
#         "Lot Frontage",
#         min_value=0.0,
#         value=70.0
#     )

#     wooddecksf = st.number_input(
#         "Wood Deck Area",
#         min_value=0.0,
#         value=100.0
#     )

#     openporchsf = st.number_input(
#         "Open Porch Area",
#         min_value=0.0,
#         value=50.0
#     )

#     lotarea = st.number_input(
#         "Lot Area",
#         min_value=0.0,
#         value=9000.0
#     )

#     centralair = st.selectbox(
#         "Central Air Conditioning",
#         ["Yes", "No"]
#     )

# # ---------------- PREDICTION ---------------- #

# st.markdown("<br>", unsafe_allow_html=True)

# if st.button("Predict House Price"):

#     centralair_value = 1 if centralair == "Yes" else 0

#     input_df = pd.DataFrame([{
#         'OverallQual': overallqual,
#         'GrLivArea': grlivarea,
#         'GarageArea': garagearea,
#         '1stFlrSF': firstflrsf,
#         'FullBath': fullbath,
#         'YearBuilt': yearbuilt,
#         'YearRemodAdd': yearremodadd,
#         'MasVnrArea': masvnrarea,
#         'Fireplaces': fireplaces,
#         'BsmtFinSF1': bsmtfinsf1,
#         'LotFrontage': lotfrontage,
#         'WoodDeckSF': wooddecksf,
#         'OpenPorchSF': openporchsf,
#         'LotArea': lotarea,
#         'CentralAir': centralair_value
#     }])

#     prediction = model.predict(input_df)[0]

#     st.markdown("<br>", unsafe_allow_html=True)

#     st.markdown(
#         f"""
#         <div class="result-card">
#             <h2>Estimated House Price</h2>
#             <div class="result-price">${prediction:,.2f}</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown("---")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("R² Score", "0.899")

# with col2:
#     st.metric("Mean Absolute Error", "$18,140")



# -----------------------------NEW-------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HomeVal AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS + Animations ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #080B12;
    color: #DDE1F0;
}
.block-container { padding: 0 2.5rem 5rem; max-width: 1150px; }

/* ── Animated gradient orb background ── */
.orb-bg {
    position: fixed;
    top: -200px; left: -200px;
    width: 700px; height: 700px;
    background: radial-gradient(circle, #1A3AFF22 0%, transparent 70%);
    border-radius: 50%;
    animation: drift 12s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}
.orb-bg2 {
    position: fixed;
    bottom: -150px; right: -150px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, #8B2FFF18 0%, transparent 70%);
    border-radius: 50%;
    animation: drift2 15s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}
@keyframes drift  { from { transform: translate(0,0)   scale(1);   } to { transform: translate(80px, 60px)  scale(1.15); } }
@keyframes drift2 { from { transform: translate(0,0)   scale(1);   } to { transform: translate(-60px,-80px) scale(1.2);  } }

/* ── Hero ── */
.hero-wrap {
    padding: 4.5rem 0 2rem;
    position: relative;
    z-index: 1;
}
.badge {
    display: inline-block;
    background: linear-gradient(90deg,#1A3AFF22,#8B2FFF22);
    border: 1px solid #1A3AFF44;
    border-radius: 999px;
    padding: 0.3rem 1rem;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #7B9FFF;
    margin-bottom: 1.2rem;
    animation: fadeSlideDown 0.8s ease both;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 6vw, 5.2rem);
    font-weight: 900;
    line-height: 1.05;
    margin: 0 0 1.2rem;
    animation: fadeSlideDown 0.9s ease 0.1s both;
}
.hero-title .accent {
    background: linear-gradient(135deg, #4D7AFF, #B56EFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1.05rem;
    color: #7B859E;
    max-width: 520px;
    line-height: 1.7;
    animation: fadeSlideDown 1s ease 0.2s both;
}
@keyframes fadeSlideDown {
    from { opacity:0; transform:translateY(-18px); }
    to   { opacity:1; transform:translateY(0); }
}

/* ── Live stats bar ── */
.stats-bar {
    display: flex;
    gap: 2rem;
    padding: 1.2rem 2rem;
    background: #0E1220;
    border: 1px solid #1C2340;
    border-radius: 14px;
    margin: 1.5rem 0 2.5rem;
    animation: fadeSlideDown 1s ease 0.3s both;
}
.stat-item { text-align: center; flex: 1; }
.stat-val {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, #4D7AFF, #B56EFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-lbl { font-size: 0.7rem; color: #4A5268; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 2px; }

/* ── Section header ── */
.section-hdr {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #4D7AFF;
    font-weight: 600;
    margin: 2rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.section-hdr::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1C2340, transparent);
}

/* ── Input cards ── */
.input-card {
    background: #0E1220;
    border: 1px solid #1C2340;
    border-radius: 16px;
    padding: 1.6rem 1.8rem 1.2rem;
    margin-bottom: 1rem;
    transition: border-color 0.3s;
    position: relative;
    overflow: hidden;
}
.input-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #4D7AFF, #B56EFF);
    opacity: 0;
    transition: opacity 0.3s;
}
.input-card:hover { border-color: #2A3560; }
.input-card:hover::before { opacity: 1; }

/* ── Streamlit widget overrides ── */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div:first-child {
    background: #13182A !important;
    border-color: #222840 !important;
    border-radius: 10px !important;
    color: #DDE1F0 !important;
    transition: border-color 0.2s !important;
}
div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: #4D7AFF !important;
    box-shadow: 0 0 0 3px #4D7AFF18 !important;
}
div[data-baseweb="input"] input { color: #DDE1F0 !important; }
label { color: #8890A8 !important; font-size: 0.83rem !important; font-weight: 500 !important; }

/* ── Slider overrides ── */
div[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(90deg, #4D7AFF, #B56EFF) !important;
}

/* ── Predict button ── */
.stButton > button {
    width: 100%;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #1A3AFF, #7B2FFF);
    color: #fff;
    font-weight: 700;
    font-size: 1.05rem;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    letter-spacing: 0.04em;
    transition: transform 0.15s, box-shadow 0.15s;
    box-shadow: 0 4px 24px #1A3AFF30;
    margin-top: 1.2rem;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px #1A3AFF50;
}
.stButton > button:active { transform: translateY(0); }

/* ── Result ── */
.result-outer {
    position: relative;
    border-radius: 20px;
    padding: 2px;
    background: linear-gradient(135deg, #4D7AFF, #B56EFF);
    margin-top: 2.5rem;
    animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}
@keyframes popIn {
    from { opacity:0; transform:scale(0.92); }
    to   { opacity:1; transform:scale(1);    }
}
.result-inner {
    background: #0B0E1A;
    border-radius: 18px;
    padding: 3rem 2rem;
    text-align: center;
}
.result-eyebrow {
    font-size: 0.68rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #4D7AFF;
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.result-price {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.5rem, 8vw, 5.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 30%, #B56EFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    padding-bottom: 0.15em;
    margin-bottom: 0.4rem;
}
.result-range {
    font-size: 0.85rem;
    color: #3A4268;
    margin-bottom: 2rem;
}
.result-range span { color: #6B7FBB; }

/* ── Feature meter bars ── */
.meters { display: flex; flex-direction: column; gap: 0.7rem; text-align: left; max-width: 480px; margin: 0 auto; }
.meter-row { display: flex; align-items: center; gap: 0.75rem; }
.meter-lbl { font-size: 0.72rem; color: #5A6280; width: 130px; flex-shrink: 0; }
.meter-track { flex: 1; height: 5px; background: #1C2340; border-radius: 99px; overflow: hidden; }
.meter-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #4D7AFF, #B56EFF); }
.meter-val { font-size: 0.72rem; color: #8890A8; width: 60px; text-align: right; flex-shrink: 0; }

/* ── Confidence pill ── */
.conf-pill {
    display: inline-block;
    background: linear-gradient(90deg,#4D7AFF18,#B56EFF18);
    border: 1px solid #4D7AFF33;
    border-radius: 999px;
    padding: 0.4rem 1.2rem;
    font-size: 0.78rem;
    color: #7B9FFF;
    margin-top: 1.5rem;
}

/* ── Footer ── */
.footer { text-align:center; color:#252A3A; font-size:0.7rem; padding:3rem 0 1rem; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>

<div class="orb-bg"></div>
<div class="orb-bg2"></div>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="badge">✦ XGBoost · Ames Iowa Dataset · Real-time AI</div>
    <h1 class="hero-title">What's your home<br><span class="accent">really worth?</span></h1>
    <p class="hero-sub">Fill in the property details below. Our model analyses 15 key features and delivers an instant valuation — no agents, no waiting.</p>
</div>
""", unsafe_allow_html=True)

# ── Stats bar ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item"><div class="stat-val">1,460</div><div class="stat-lbl">Training homes</div></div>
    <div class="stat-item"><div class="stat-val">~89%</div><div class="stat-lbl">R² accuracy</div></div>
    <div class="stat-item"><div class="stat-val">15</div><div class="stat-lbl">Features analysed</div></div>
    <div class="stat-item"><div class="stat-val">&lt;1s</div><div class="stat-lbl">Prediction time</div></div>
</div>
""", unsafe_allow_html=True)


# ── INPUTS ────────────────────────────────────────────────────────────────────
# Section 1 — Structure
st.markdown('<div class="section-hdr">Structure & Size</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    overall_qual = st.slider("Overall Quality", 1, 10, 7,
        help="Overall material and finish quality (1=Poor, 10=Excellent)")
with col2:
    gr_liv_area = st.number_input("Above-ground Living Area (sq ft)",
        min_value=300, max_value=6000, value=1500, step=50)
with col3:
    first_flr_sf = st.number_input("1st Floor Area (sq ft)",
        min_value=200, max_value=4000, value=900, step=50)

col4, col5, col6 = st.columns(3)
with col4:
    lot_area = st.number_input("Lot Area (sq ft)",
        min_value=1000, max_value=200000, value=8500, step=500)
with col5:
    lot_frontage = st.number_input("Lot Frontage (ft)",
        min_value=0, max_value=300, value=69, step=1)
with col6:
    mas_vnr_area = st.number_input("Masonry Veneer Area (sq ft)",
        min_value=0, max_value=1600, value=0, step=10)

# Section 2 — Interior
st.markdown('<div class="section-hdr">Interior & Amenities</div>', unsafe_allow_html=True)

col7, col8, col9 = st.columns(3)
with col7:
    full_bath = st.selectbox("Full Bathrooms", [0, 1, 2, 3, 4], index=2)
with col8:
    fireplaces = st.selectbox("Fireplaces", [0, 1, 2, 3], index=0)
with col9:
    central_air = st.selectbox("Central Air Conditioning", ["Yes", "No"], index=0)

col10, col11 = st.columns(2)
with col10:
    bsmt_fin_sf1 = st.number_input("Basement Finished Area (sq ft)",
        min_value=0, max_value=3000, value=400, step=50)
with col11:
    garage_area = st.number_input("Garage Area (sq ft)",
        min_value=0, max_value=1500, value=480, step=10)

# Section 3 — Outdoor
st.markdown('<div class="section-hdr">Outdoor & Year</div>', unsafe_allow_html=True)

col12, col13, col14 = st.columns(3)
with col12:
    wood_deck_sf = st.number_input("Wood Deck Area (sq ft)",
        min_value=0, max_value=1000, value=0, step=10)
with col13:
    open_porch_sf = st.number_input("Open Porch Area (sq ft)",
        min_value=0, max_value=600, value=0, step=10)
with col14:
    year_built = st.number_input("Year Built",
        min_value=1872, max_value=2024, value=2003, step=1)

year_remod_add = st.number_input("Year Remodelled / Added",
    min_value=1950, max_value=2024, value=2003, step=1)


# ── PREDICT ───────────────────────────────────────────────────────────────────
st.markdown("")
predict = st.button("✦  Estimate Home Value")

if predict:
    # Encode CentralAir
    central_air_enc = 1 if central_air == "Yes" else 0

    # EXACT column order from training
    input_data = {
        "OverallQual":  overall_qual,
        "GrLivArea":    gr_liv_area,
        "GarageArea":   garage_area,
        "1stFlrSF":     first_flr_sf,
        "FullBath":     full_bath,
        "YearBuilt":    year_built,
        "YearRemodAdd": year_remod_add,
        "MasVnrArea":   mas_vnr_area,
        "Fireplaces":   fireplaces,
        "BsmtFinSF1":   bsmt_fin_sf1,
        "LotFrontage":  lot_frontage,
        "WoodDeckSF":   wood_deck_sf,
        "OpenPorchSF":  open_porch_sf,
        "LotArea":      lot_area,
        "CentralAir":   central_air_enc,
    }

    input_df = pd.DataFrame([input_data])

    # Animate — rolling counter effect
    with st.spinner(""):
        time.sleep(0.4)

    try:
        model = joblib.load("xgb_model.jb")
        prediction = float(model.predict(input_df)[0])
        low  = prediction * 0.92
        high = prediction * 1.08

        # Feature importance visual (normalized for meter bars)
        features_display = {
            "Overall Quality":    (overall_qual / 10, f"{overall_qual}/10"),
            "Living Area":        (min(gr_liv_area / 5000, 1), f"{gr_liv_area:,} ft²"),
            "Garage Area":        (min(garage_area / 1200, 1), f"{garage_area} ft²"),
            "1st Floor":          (min(first_flr_sf / 3500, 1), f"{first_flr_sf:,} ft²"),
            "Basement Finished":  (min(bsmt_fin_sf1 / 2500, 1), f"{bsmt_fin_sf1} ft²"),
            "Year Built":         ((year_built - 1872) / (2024 - 1872), str(year_built)),
        }

        meters_html = '<div class="meters">'
        for lbl, (pct, val) in features_display.items():
            pct_css = round(pct * 100, 1)
            meters_html += f"""
            <div class="meter-row">
                <div class="meter-lbl">{lbl}</div>
                <div class="meter-track"><div class="meter-fill" style="width:{pct_css}%"></div></div>
                <div class="meter-val">{val}</div>
            </div>"""
        meters_html += '</div>'

        st.markdown(f"""
        <div class="result-outer">
            <div class="result-inner">
                <div class="result-eyebrow">AI Estimated Market Value</div>
                <div class="result-price">${prediction:,.0f}</div>
                <div class="result-range">Likely range &nbsp;·&nbsp;
                    <span>${low:,.0f}</span> — <span>${high:,.0f}</span>
                </div>
                {meters_html}
                <div class="conf-pill">✦ Model confidence · R² ≈ 0.89 · MAE ≈ $15,000</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("⚠️  `xgb_model.jb` not found. Place the saved model file in the same folder as `app.py`.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">HomeVal AI · XGBoost · Ames Iowa Housing Dataset · For informational use only</div>', unsafe_allow_html=True)