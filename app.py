import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


if not hasattr(np, 'float'):
    np.float = float
    np.int = int
    np.bool = bool

# --- Setup Streamlit page config ---
st.set_page_config(
    page_title="Nepal Climate and Development Dashboard",
    page_icon="🌏",
    layout="wide",
)

# --- App Title and Introduction ---
st.title("🌏 Nepal Climate and Development Dashboard")
st.markdown("""
Welcome to the Multi-Domain Dashboard analyzing various sectors like:
- 🌦️ Weather and Climate
- 🌱 Environmental Indicators
- 🏛️ Socioeconomic Development
- 🏔️ Glacier Monitoring and Prediction
- 🧠 Machine Learning and Environmental AI

Use the sidebar to navigate!
""")

# --- Optimized Sidebar Navigation ---
st.sidebar.title("🌍 Nepal Dashboard Navigation")
st.sidebar.markdown("## 📂 Select a Domain")

domain_options = {
    "🌦️ Climate / Weather": [
        "📈 Yearly Extreme Event Trends",
        "🗺️ District-Wise Weather Map",
        "📐 Mann-Kendall Weather Test",
        "📉 Sen's Slope Weather Trend",
        "📖 About Climate Module"
    ],
    "🌱 Environmental Indicators": [
        "🌳 Forest Cover Trends",
        "🌫️ Glacier Formation",
        "🚰 Water Resource Health",
        "📖 About Environment Module"
    ],
    "🏛️ Socioeconomic Indicators": [
        "📈 Agricultural Yield Trends",
        "👥 Population Distribution",
        "🌊 Economic Loss Forecast",
        "📖 About Socioeconomic Module"

    ],
    "🏔️ Glacier Monitoring": [
        "📊 Historical Glacier Trends",
        "🔮 Forecast Glacier Melt",
        "📈 Model Evaluation",
        "📖 About Glacier Module"
    ],
    "🧠 Machine Learning Models": [
        "📈 Model Performance Summary",
        "📊 Feature Trends"
    ]
}

# --- Domain and Page Selection ---
domain = st.sidebar.selectbox("Choose Analysis Domain", list(domain_options.keys()))
page = st.sidebar.radio("Select Report", domain_options[domain])

# --- Domain and Page Actions ---

# Climate / Weather Domain
if domain == "🌦️ Climate / Weather":
    if page == "📈 Yearly Extreme Event Trends":
        from modules.weather.trend_overview import show_trend_chart_weather
        show_trend_chart_weather()

    elif page == "🗺️ District-Wise Weather Map":
        from modules.weather.map_view import show_map
        show_map()

    elif page == "📐 Mann-Kendall Weather Test":
        from modules.weather.mann_kendall_summary import show_mk_results
        show_mk_results()

    elif page == "📉 Sen's Slope Weather Trend":
        from modules.weather.sen_slope import show_sen_plot
        show_sen_plot()

    elif page == "📖 About Climate Module":
        from modules.weather.about import show_about
        show_about()

# Environmental Indicators Domain
elif domain == "🌱 Environmental Indicators":
    if page == "🌳 Forest Cover Trends":
        from modules.environment.forest_loss_trend import show_forest_loss_trend
        show_forest_loss_trend()

    elif page == "🌫️ Glacier Formation":
        from modules.environment.glacier_formation_trend import show_glacier_formation_trend
        show_glacier_formation_trend()

    elif page == "🚰 Water Resource Health":
        from modules.environment.water_health import show_water_health
        show_water_health()

    elif page == "📖 About Environment Module":
        from modules.environment.about import show_about_environment
        show_about_environment()


# Socioeconomic Indicators Domain
elif domain == "🏛️ Socioeconomic Indicators":
    if page == "📈 Agricultural Yield Trends":
        from modules.socioeconomic.agriculture_yield_trend import show_agricultural_yield
        show_agricultural_yield()

    elif page == "👥 Population Distribution":
        from modules.socioeconomic.population_distribution import show_population_distribution
        show_population_distribution()

    elif page == "🌊 Economic Loss Forecast":
        from modules.socioeconomic.economic_loss_forecast import show_economic_loss_forecast
        show_economic_loss_forecast()

    elif page == "📖 About Socioeconomic Module":
        from modules.socioeconomic.about import show_about_socioeconomic
        show_about_socioeconomic()




# Glacier Monitoring Domain
elif domain == "🏔️ Glacier Monitoring":
    if page == "📊 Historical Glacier Trends":
        from modules.glacier.historical_trend import show_historical_trend
        show_historical_trend()

    elif page == "🔮 Forecast Glacier Melt":
        from modules.glacier.forecast_melt import show_forecast
        show_forecast()

    elif page == "📈 Model Evaluation":
        from modules.glacier.model_evaluation import show_model_evaluation
        show_model_evaluation()

    elif page == "📖 About Glacier Module":
        from modules.glacier.about import show_about_glacier
        show_about_glacier()

# Machine Learning Models Domain
elif domain == "🧠 Machine Learning Models":
    if page == "📈 Model Performance Summary":
        from modules.machine_learning.model_performance_summary import show_model_summary
        show_model_summary()

    elif page == "📊 Feature Trends":
        from modules.machine_learning.feature_trends import show_feature_trends
        show_feature_trends()



# Error Handling
else:
    st.warning("⚠️ Please select a valid Domain and Report.")
