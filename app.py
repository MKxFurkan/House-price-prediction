import pandas as pd
import streamlit as st
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stApp {
    background-color: #0E1117;
}

.big-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #A0A0A0;
    margin-bottom: 30px;
}

.result-card {
    background-color: #1C1F26;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #2E3440;
}

.result-price {
    font-size: 2.2rem;
    font-weight: bold;
    color: #00E676;
}

.metric-card {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #2E3440;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MODEL ---------------- #

model = joblib.load("xgb_model.jb")

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("""
<style>

.info-card {
    background: linear-gradient(135deg, #1e293b, #334155);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 15px rgba(59,130,246,0.25);
    animation: glow 3s infinite alternate;
}

@keyframes glow {
    from {
        box-shadow: 0 0 10px rgba(59,130,246,0.20);
    }
    to {
        box-shadow: 0 0 25px rgba(59,130,246,0.60);
    }
}

.info-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}

.info-item {
    font-size: 16px;
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)


st.sidebar.markdown("""
# 🏠 House Price Predictor
### Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.markdown("## Model Status ")

st.sidebar.success(
    "Machine Learning Model Loaded Successfully"
)

st.sidebar.markdown("---")

st.sidebar.title("Model Details")

st.sidebar.metric("R² Score", "0.899")
st.sidebar.metric("MAE", "$18,140")
st.sidebar.metric("Algorithm", "XGBoost")

# ---------------- HEADER ---------------- #

st.markdown(
    '<div class="big-title">🏠 House Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict house prices using an XGBoost Machine Learning Model</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT SECTION ---------------- #

col1, col2 = st.columns(2)

with col1:
    overallqual = st.slider("Overall Quality (1-10)", 1, 10, 5)

    grlivarea = st.number_input(
        "Living Area (sq ft)",
        min_value=0.0,
        value=1500.0
    )

    garagearea = st.number_input(
        "Garage Area (sq ft)",
        min_value=0.0,
        value=500.0
    )

    firstflrsf = st.number_input(
        "First Floor Area (sq ft)",
        min_value=0.0,
        value=1200.0
    )

    fullbath = st.number_input(
        "Number of Full Bathrooms",
        min_value=0,
        value=2
    )

    yearbuilt = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    yearremodadd = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    masvnrarea = st.number_input(
        "Masonry Veneer Area",
        min_value=0.0,
        value=100.0
    )

with col2:
    fireplaces = st.number_input(
        "Number of Fireplaces",
        min_value=0,
        value=1
    )

    bsmtfinsf1 = st.number_input(
        "Finished Basement Area",
        min_value=0.0,
        value=500.0
    )

    lotfrontage = st.number_input(
        "Lot Frontage",
        min_value=0.0,
        value=70.0
    )

    wooddecksf = st.number_input(
        "Wood Deck Area",
        min_value=0.0,
        value=100.0
    )

    openporchsf = st.number_input(
        "Open Porch Area",
        min_value=0.0,
        value=50.0
    )

    lotarea = st.number_input(
        "Lot Area",
        min_value=0.0,
        value=9000.0
    )

    centralair = st.selectbox(
        "Central Air Conditioning",
        ["Yes", "No"]
    )

# ---------------- PREDICTION ---------------- #

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Predict House Price"):

    centralair_value = 1 if centralair == "Yes" else 0

    input_df = pd.DataFrame([{
        'OverallQual': overallqual,
        'GrLivArea': grlivarea,
        'GarageArea': garagearea,
        '1stFlrSF': firstflrsf,
        'FullBath': fullbath,
        'YearBuilt': yearbuilt,
        'YearRemodAdd': yearremodadd,
        'MasVnrArea': masvnrarea,
        'Fireplaces': fireplaces,
        'BsmtFinSF1': bsmtfinsf1,
        'LotFrontage': lotfrontage,
        'WoodDeckSF': wooddecksf,
        'OpenPorchSF': openporchsf,
        'LotArea': lotarea,
        'CentralAir': centralair_value
    }])

    prediction = model.predict(input_df)[0]

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="result-card">
            <h2>Estimated House Price</h2>
            <div class="result-price">${prediction:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", "0.899")

with col2:
    st.metric("Mean Absolute Error", "$18,140")