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

# ── Theme palettes (light + dark) ─────────────────────────────────────────────
# Your palette: #345C32 · #9CAC54 · #97CD97
# Extra tones (very light tints for light mode, very dark shades for dark mode and
# text) are derived from the same green hue for contrast.
LIGHT = {
    "scheme": "light",
    "bg": "#EAF3E2",        "card": "#DCEBD3",      "card2": "#C3E3C3",
    "border": "#C3E3C3",    "border2": "#97CD97",
    "ink": "#1F3A1E",       "muted": "#4A6B48",     "label": "#3B5A39",
    "accent": "#345C32",
    "g1": "#345C32",        "g2": "#9CAC54",
    "fill1": "#97CD97",     "fill2": "#345C32",
    "price1": "#1F3A1E",    "price2": "#345C32",
    "orb1": "#97CD9755",    "orb2": "#9CAC5444",
    "btn1": "#97CD97",      "btn2": "#9CAC54",      "btntxt": "#1F3A1E",
    "badge1": "#C3E3C3",    "badge2": "#DCEBD3",    "badgetxt": "#345C32",
    "pill1": "#C3E3C3",     "pill2": "#EAF3E2",     "pilltxt": "#345C32",
    "ring": "#97CD9760",    "shadow": "#97CD9770",  "shadow2": "#97CD97aa",
    "thumb": "#345C32",     "track": "#EAF3E2",
}
DARK = {
    "scheme": "dark",
    "bg": "#121C12",        "card": "#1B2A1B",      "card2": "#2A4A2A",
    "border": "#2C4A2B",    "border2": "#4C7F49",
    "ink": "#EAF5E6",       "muted": "#A9C2A4",     "label": "#C3D8BE",
    "accent": "#97CD97",
    "g1": "#97CD97",        "g2": "#9CAC54",
    "fill1": "#97CD97",     "fill2": "#9CAC54",
    "price1": "#ffffff",    "price2": "#97CD97",
    "orb1": "#97CD9730",    "orb2": "#9CAC5422",
    "btn1": "#97CD97",      "btn2": "#9CAC54",      "btntxt": "#121C12",
    "badge1": "#264A26",    "badge2": "#1B2A1B",    "badgetxt": "#97CD97",
    "pill1": "#264A26",     "pill2": "#1B2A1B",     "pilltxt": "#97CD97",
    "ring": "#97CD9740",    "shadow": "#97CD9740",  "shadow2": "#97CD9770",
    "thumb": "#97CD97",     "track": "#121C12",
}

# ── Global CSS + Animations (all colours come from CSS variables) ─────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--ink);
}
.stApp, [data-testid="stAppViewContainer"] { background: var(--bg) !important; color: var(--ink); }
.block-container { padding: 0 2.5rem 5rem; max-width: 1150px; }

/* ── Animated gradient orb background ── */
.orb-bg {
    position: fixed;
    top: -200px; left: -200px;
    width: 700px; height: 700px;
    background: radial-gradient(circle, var(--orb1) 0%, transparent 70%);
    border-radius: 50%;
    animation: drift 12s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}
.orb-bg2 {
    position: fixed;
    bottom: -150px; right: -150px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, var(--orb2) 0%, transparent 70%);
    border-radius: 50%;
    animation: drift2 15s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}
@keyframes drift  { from { transform: translate(0,0)   scale(1);   } to { transform: translate(80px, 60px)  scale(1.15); } }
@keyframes drift2 { from { transform: translate(0,0)   scale(1);   } to { transform: translate(-60px,-80px) scale(1.2);  } }

/* ── Hero ── */
.hero-wrap {
    padding: 1.5rem 0 2rem;
    position: relative;
    z-index: 1;
}
.badge {
    display: inline-block;
    background: linear-gradient(90deg, var(--badge1), var(--badge2));
    border: 1px solid var(--border2);
    border-radius: 999px;
    padding: 0.3rem 1rem;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--badgetxt);
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
.stApp h1.hero-title, h1.hero-title {
    color: var(--ink) !important;
    -webkit-text-fill-color: var(--ink);
}
.hero-title .accent {
    background: linear-gradient(135deg, var(--g1), var(--g2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent !important;
    background-clip: text;
}
.hero-sub {
    font-size: 1.05rem;
    color: var(--muted);
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
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    margin: 1.5rem 0 2.5rem;
    animation: fadeSlideDown 1s ease 0.3s both;
}
.stat-item { text-align: center; flex: 1; }
.stat-val {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    font-variant-numeric: lining-nums;
    color: var(--accent);
}
.stat-lbl { font-size: 0.7rem; color: var(--label); font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 2px; }

/* ── Section header ── */
.section-hdr {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--accent);
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
    background: linear-gradient(90deg, var(--border2), transparent);
}

/* ── Input cards ── */
.input-card {
    background: var(--card);
    border: 1px solid var(--border);
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
    background: linear-gradient(90deg, var(--border2), var(--card2));
    opacity: 0;
    transition: opacity 0.3s;
}
.input-card:hover { border-color: var(--border2); }
.input-card:hover::before { opacity: 1; }

/* ── Streamlit widget overrides ── */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div:first-child {
    background: var(--card) !important;
    border-color: var(--border2) !important;
    border-radius: 10px !important;
    color: var(--ink) !important;
    transition: border-color 0.2s !important;
}
div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--ring) !important;
}
div[data-baseweb="input"] input { color: var(--ink) !important; }
div[data-baseweb="select"] div, div[data-baseweb="select"] span { color: var(--ink) !important; }
div[data-baseweb="select"] svg { fill: var(--ink) !important; }
label, label p { color: var(--label) !important; font-size: 0.83rem !important; font-weight: 500 !important; }

/* ── Dropdown menu (selectbox) ── */
div[data-baseweb="popover"] > div,
ul[role="listbox"] { background: var(--card) !important; }
li[role="option"] { background: var(--card) !important; color: var(--ink) !important; }
li[role="option"]:hover, li[aria-selected="true"] { background: var(--card2) !important; }

/* ── Number input (+ / − buttons) ── */
div[data-testid="stNumberInputContainer"] {
    background: var(--card) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 10px !important;
    overflow: hidden;
}
div[data-testid="stNumberInputContainer"] > div { border: none !important; }
div[data-testid="stNumberInput"] button {
    background: var(--card2) !important;
    color: var(--ink) !important;
    border: none !important;
}
div[data-testid="stNumberInput"] button:hover:not(:disabled) { background: var(--border2) !important; }
div[data-testid="stNumberInput"] button:disabled { opacity: 0.4; }
div[data-testid="stNumberInput"] button svg { fill: var(--ink) !important; color: var(--ink) !important; }
div[data-testid="stNumberInput"] input { color: var(--ink) !important; font-weight: 500; }

/* ── Slider overrides ── */
div[data-baseweb="slider"] div[role="slider"] {
    background: var(--thumb) !important;
    border-color: var(--thumb) !important;
    box-shadow: 0 0 0 4px var(--ring) !important;
}
div[data-testid="stSliderThumbValue"],
div[data-testid="stSlider"] [data-testid="stThumbValue"] {
    color: var(--accent) !important;
    font-weight: 700 !important;
}
div[data-testid="stSliderTickBarMin"],
div[data-testid="stSliderTickBarMax"] { color: var(--label) !important; }

/* ── Predict button ── */
.stButton > button {
    width: 100%;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, var(--btn1), var(--btn2));
    color: var(--btntxt);
    font-weight: 700;
    font-size: 1.05rem;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    letter-spacing: 0.04em;
    transition: transform 0.15s, box-shadow 0.15s;
    box-shadow: 0 4px 24px var(--shadow);
    margin-top: 1.2rem;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px var(--shadow2);
    color: var(--btntxt);
}
.stButton > button:active { transform: translateY(0); }

/* ── Result ── */
.result-outer {
    position: relative;
    border-radius: 20px;
    padding: 2px;
    background: linear-gradient(135deg, var(--btn1), var(--btn2));
    margin-top: 2.5rem;
    animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}
@keyframes popIn {
    from { opacity:0; transform:scale(0.92); }
    to   { opacity:1; transform:scale(1);    }
}
.result-inner {
    background: var(--card);
    border-radius: 18px;
    padding: 3rem 2rem;
    text-align: center;
}
.result-eyebrow {
    font-size: 0.68rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.result-price {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.5rem, 8vw, 5.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, var(--price1) 30%, var(--price2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    padding-bottom: 0.15em;
    margin-bottom: 0.4rem;
}
.result-range {
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 2rem;
}
.result-range span { color: var(--ink); }

/* ── Feature meter bars ── */
.meters { display: flex; flex-direction: column; gap: 0.7rem; text-align: left; max-width: 480px; margin: 0 auto; }
.meter-row { display: flex; align-items: center; gap: 0.75rem; }
.meter-lbl { font-size: 0.72rem; color: var(--muted); width: 130px; flex-shrink: 0; }
.meter-track { flex: 1; height: 5px; background: var(--track); border-radius: 99px; overflow: hidden; }
.meter-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--fill1), var(--fill2)); }
.meter-val { font-size: 0.72rem; color: var(--label); width: 60px; text-align: right; flex-shrink: 0; }

/* ── Confidence pill ── */
.conf-pill {
    display: inline-block;
    background: linear-gradient(90deg, var(--pill1), var(--pill2));
    border: 1px solid var(--border2);
    border-radius: 999px;
    padding: 0.4rem 1.2rem;
    font-size: 0.78rem;
    color: var(--pilltxt);
    margin-top: 1.5rem;
}

/* ── Footer ── */
.footer { text-align:center; color:var(--muted); font-size:0.7rem; padding:3rem 0 1rem; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>

<div class="orb-bg"></div>
<div class="orb-bg2"></div>
""", unsafe_allow_html=True)

# ── Dark mode toggle (top right) ──────────────────────────────────────────────
_sp, _tg = st.columns([5, 1])
with _tg:
    dark_mode = st.toggle("🌙 Dark mode", value=False, key="dark_mode")

theme = DARK if dark_mode else LIGHT
_vars = ";".join(f"--{k}:{v}" for k, v in theme.items() if k != "scheme")
st.markdown(
    f"<style>:root{{{_vars};color-scheme:{theme['scheme']};}}</style>",
    unsafe_allow_html=True,
)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="badge">✦ XGBoost · Ames Iowa Dataset · Real-time AI</div>
    <h1 class="hero-title">What's your home<br><span class="accent">really worth?</span></h1>
    <p class="hero-sub">Fill in the property details below. This model analyses 15 key features and delivers an instant valuation — no agents, no waiting.</p>
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