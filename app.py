import streamlit as st

# Setup Streamlit page config
st.set_page_config(
    page_title="Nepal Climate and Development Dashboard",
    page_icon="🌏",
    layout="wide",
)

# App Title and Introduction
st.title("🌏 Nepal Climate and Development Dashboard")
st.markdown("""
Welcome to the Multi-Domain Dashboard analyzing various sectors like:
- 🌦️ Weather and Climate
- 🌱 Environmental Indicators
- 🏛️ Socioeconomic Development

Use the sidebar to navigate!
""")

# Sidebar - First Select Domain
st.sidebar.title("Select Analysis Domain")

domain = st.sidebar.selectbox("Choose a Domain", [
    "🌦️ Climate / Weather",
    "🌱 Environmental Indicators",
    "🏛️ Socioeconomic Indicators"
])

# Sidebar - Then Select Page based on Domain
if domain == "🌦️ Climate / Weather":
    page = st.sidebar.radio("Weather Reports", [
        "📈 Yearly Extreme Event Trends",
        "🗺️ District-Wise Weather Map",
        "📐 Mann-Kendall Weather Test",
        "📉 Sen's Slope Weather Trend",
        "📖 About Climate Module"
    ])

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

elif domain == "🌱 Environmental Indicators":
    page = st.sidebar.radio("Environmental Reports", [
        "🌳 Forest Cover Trends",
        "🌫️ Air Quality Analysis",
        "🚰 Water Resource Health",
        "📖 About Environment Module"
    ])

    if page == "🌳 Forest Cover Trends":
        from modules.environment.forest_trend import show_forest_trend
        show_forest_trend()

    elif page == "🌫️ Air Quality Analysis":
        from modules.environment.air_quality import show_air_quality
        show_air_quality()

    elif page == "🚰 Water Resource Health":
        from modules.environment.water_health import show_water_health
        show_water_health()

    elif page == "📖 About Environment Module":
        from modules.environment.about import show_about_environment
        show_about_environment()

elif domain == "🏛️ Socioeconomic Indicators":
    page = st.sidebar.radio("Socioeconomic Reports", [
        "🏫 Education Trends",
        "🏥 Health Access Analysis",
        "💼 Employment Rate Analysis",
        "📖 About Socioeconomic Module"
    ])

    if page == "🏫 Education Trends":
        from modules.socioeconomic.education_trend import show_education_trend
        show_education_trend()

    elif page == "🏥 Health Access Analysis":
        from modules.socioeconomic.health_access import show_health_access
        show_health_access()

    elif page == "💼 Employment Rate Analysis":
        from modules.socioeconomic.employment_rate import show_employment_rate
        show_employment_rate()

    elif page == "📖 About Socioeconomic Module":
        from modules.socioeconomic.about import show_about_socioeconomic
        show_about_socioeconomic()


else:
    st.warning("⚠️ Please select a valid Domain and Report.")
