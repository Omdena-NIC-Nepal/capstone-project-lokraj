import streamlit as st

st.set_page_config(page_title="Climate Change Dashboard - Nepal", layout="wide")

st.title("🌍 Climate Change Impact Assessment Dashboard")

st.markdown("""
Welcome to the central hub for analyzing and predicting the impacts of climate change in Nepal.

Use the sidebar to navigate through various modules:
- 📊 Weather & Climate Data
- 🛰️ Environmental Data
- 👥 Socioeconomic Data
- 🤖 Machine Learning Models
- 🗣️ NLP for Climate Reports
- 📈 Model Evaluation & Deployment
""")

st.header("🔍 Project Objective")
st.info("""
To build a modular, data-driven system for monitoring, analyzing, and forecasting climate change
impacts in Nepal, with a focus on data integration and stakeholder usability.
""")

st.header("📦 Modules Overview")
st.markdown("""
Navigate to any of the modules via the **left sidebar**. Each module includes:
- Data Loading & Cleaning
- Exploratory Analysis
- Feature Engineering
- Machine Learning
- Evaluation & Dashboarding
- Documentation
""")

# pages/1_Weather_Climate_Data.py
import streamlit as st

st.title("📊 Weather & Climate Data")
st.markdown("Analyze historical weather trends, glacial monitoring, and reanalysis data.")

section = st.sidebar.radio("Select Submodule", [
    "📈 Historical DHM Data",
    "🛰️ NASA Satellite Imagery",
    "📍 WMO Weather Station Data",
    "🌡️ ERA5 Climate Reanalysis"
])

if section == "📈 Historical DHM Data":
    st.subheader("1. Historical DHM Data")
    st.markdown("""
    - Step 1: Upload and preprocess historical temperature/precipitation datasets
    - Step 2: Perform EDA and visualize long-term trends
    - Step 3: Feature engineering (seasonal indices, anomalies)
    - Step 4: Model temperature prediction
    - Step 5: Evaluate prediction accuracy
    """)
    # Placeholder for data upload and preview
    uploaded = st.file_uploader("Upload DHM CSV/XLSX", type=["csv", "xlsx"])
    if uploaded:
        st.success("File uploaded successfully!")

elif section == "🛰️ NASA Satellite Imagery":
    st.subheader("2. Satellite Imagery for Glacial Monitoring")
    st.markdown("""
    - Step 1: Upload satellite imagery
    - Step 2: Extract glacial coverage
    - Step 3: Analyze retreat over time
    - Step 4: Predict future melt regions
    - Step 5: Display geospatial analysis
    """)

elif section == "📍 WMO Weather Station Data":
    st.subheader("3. WMO Weather Station Data")
    st.markdown("""
    - Step 1: Upload station data
    - Step 2: Map coordinates
    - Step 3: Cluster stations by altitude
    - Step 4: Analyze station-wise trends
    - Step 5: Classification of vulnerable zones
    """)

elif section == "🌡️ ERA5 Climate Reanalysis":
    st.subheader("4. ERA5 Climate Reanalysis")
    st.markdown("""
    - Step 1: Load ERA5 NetCDF files
    - Step 2: Visualize monthly/yearly anomalies
    - Step 3: Build climate index predictors
    - Step 4: Model climate trends using ML
    - Step 5: Integrate with dashboard
    """)
