# import streamlit as st

# # Setup Streamlit page config
# st.set_page_config(
#     page_title="Nepal Climate and Development Dashboard",
#     page_icon="🌏",
#     layout="wide",
# )

# # App Title and Introduction
# st.title("🌏 Nepal Climate and Development Dashboard")
# st.markdown("""
# Welcome to the Multi-Domain Dashboard analyzing various sectors like:
# - 🌦️ Weather and Climate
# - 🌱 Environmental Indicators 
# - 🏛️ Socioeconomic Development
# - 🏔️ Glacier Monitoring and Prediction

# Use the sidebar to navigate!
# """)

# # Sidebar - First Select Domain
# st.sidebar.title("Select Analysis Domain")

# domain = st.sidebar.selectbox("Choose a Domain", [
#     "🌦️ Climate / Weather",
#     "🌱 Environmental Indicators",
#     "🏛️ Socioeconomic Indicators",
#     "🏔️ Glacier Monitoring"
# ])

# # Sidebar - Then Select Page based on Domain
# if domain == "🌦️ Climate / Weather":
#     page = st.sidebar.radio("Weather Reports", [
#         "📈 Yearly Extreme Event Trends",
#         "🗺️ District-Wise Weather Map",
#         "📐 Mann-Kendall Weather Test",
#         "📉 Sen's Slope Weather Trend",
#         "📖 About Climate Module"
#     ])

#     if page == "📈 Yearly Extreme Event Trends":
#         from modules.weather.trend_overview import show_trend_chart_weather
#         show_trend_chart_weather()

#     elif page == "🗺️ District-Wise Weather Map":
#         from modules.weather.map_view import show_map
#         show_map()

#     elif page == "📐 Mann-Kendall Weather Test":
#         from modules.weather.mann_kendall_summary import show_mk_results
#         show_mk_results()

#     elif page == "📉 Sen's Slope Weather Trend":
#         from modules.weather.sen_slope import show_sen_plot
#         show_sen_plot()

#     elif page == "📖 About Climate Module":
#         from modules.weather.about import show_about
#         show_about()

# elif domain == "🌱 Environmental Indicators":
#     page = st.sidebar.radio("Environmental Reports", [
#         "🌳 Forest Cover Trends",
#         "🌫️ Air Quality Analysis",
#         "🚰 Water Resource Health",
#         "📖 About Environment Module"
#     ])

#     if page == "🌳 Forest Cover Trends":
#         from modules.environment.forest_trend import show_forest_trend
#         show_forest_trend()

#     elif page == "🌫️ Air Quality Analysis":
#         from modules.environment.air_quality import show_air_quality
#         show_air_quality()

#     elif page == "🚰 Water Resource Health":
#         from modules.environment.water_health import show_water_health
#         show_water_health()

#     elif page == "📖 About Environment Module":
#         from modules.environment.about import show_about_environment
#         show_about_environment()

# elif domain == "🏛️ Socioeconomic Indicators":
#     page = st.sidebar.radio("Socioeconomic Reports", [
#         "🏫 Education Trends",
#         "🏥 Health Access Analysis",
#         "💼 Employment Rate Analysis",
#         "📖 About Socioeconomic Module"
#     ])

#     if page == "🏫 Education Trends":
#         from modules.socioeconomic.education_trend import show_education_trend
#         show_education_trend()

#     elif page == "🏥 Health Access Analysis":
#         from modules.socioeconomic.health_access import show_health_access
#         show_health_access()

#     elif page == "💼 Employment Rate Analysis":
#         from modules.socioeconomic.employment_rate import show_employment_rate
#         show_employment_rate()

#     elif page == "📖 About Socioeconomic Module":
#         from modules.socioeconomic.about import show_about_socioeconomic
#         show_about_socioeconomic()

# elif domain == "🏔️ Glacier Monitoring":
#     page = st.sidebar.radio("Glacier Monitoring Reports", [
#         "📊 Historical Glacier Trends",
#         "🔮 Forecast Glacier Melt",
#         "📈 Model Evaluation",
#         "📖 About Glacier Module"
#     ])

#     if page == "📊 Historical Glacier Trends":
#         from modules.glacier.historical_trend import show_historical_trend
#         show_historical_trend()

#     elif page == "🔮 Forecast Glacier Melt":
#         from modules.glacier.forecast_melt import show_forecast
#         show_forecast()

#     elif page == "📈 Model Evaluation":
#         from modules.glacier.model_evaluation import show_model_evaluation
#         show_model_evaluation()

#     elif page == "📖 About Glacier Module":
#         from modules.glacier.about import show_about_glacier
#         show_about_glacier()

# elif domain == "🧠 Machine Learning Models":
#     page = st.sidebar.radio("ML Reports", [
#         "📈 Model Performance Summary",
#         "📊 Feature Trends"
#     ])

#     if page == "📈 Model Performance Summary":
#         st.title("📈 Machine Learning Model Performance Summary")

#         import pandas as pd
#         import matplotlib.pyplot as plt
#         import seaborn as sns

#         sns.set_theme(style="whitegrid")

#         # Load your modeling summary
#         BASE_DIR = "../data/Environmental/processed_combined/"
#         model_results_path = BASE_DIR + "modeling_summary.csv"
#         df_results = pd.read_csv(model_results_path)

#         st.subheader("Modeling Summary Table")
#         st.dataframe(df_results)

#         metric = st.selectbox("Select Metric to Plot:", ["Accuracy", "F1 Score", "RMSE", "MAE", "R2"])

#         if metric in df_results.columns:
#             plt.figure(figsize=(12,6))
#             sns.barplot(data=df_results[df_results['Status'] == '✅ Modeled'], x='Event', y=metric, hue='Model')
#             plt.title(f"{metric} Comparison Across Models")
#             plt.xticks(rotation=45)
#             plt.grid(True)
#             st.pyplot(plt.gcf())
#         else:
#             st.warning(f"Metric {metric} not available!")

#     elif page == "📊 Feature Trends":
#         st.title("📊 Feature Trends Over Time")

#         # Load your engineered features
#         scaled_features_path = BASE_DIR + "environmental_features_scaled.csv"
#         df_scaled = pd.read_csv(scaled_features_path)

#         feature_to_plot = st.selectbox("Select a Feature to Explore:", [col for col in df_scaled.columns if col.startswith('scaled_')])

#         plt.figure(figsize=(10,5))
#         sns.lineplot(data=df_scaled, x='Year', y=feature_to_plot)
#         plt.title(f"Trend of {feature_to_plot}")
#         plt.grid(True)
#         st.pyplot(plt.gcf())



# else:
#     st.warning("⚠️ Please select a valid Domain and Report.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
        "🌫️ Air Quality Analysis",
        "🚰 Water Resource Health",
        "📖 About Environment Module"
    ],
    "🏛️ Socioeconomic Indicators": [
        "🏫 Education Trends",
        "🏥 Health Access Analysis",
        "💼 Employment Rate Analysis",
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

# Socioeconomic Indicators Domain
elif domain == "🏛️ Socioeconomic Indicators":
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
    BASE_DIR = "../data/Environmental/processed_combined/"

    if page == "📈 Model Performance Summary":
        st.title("📈 Machine Learning Model Performance Summary")

        model_results_path = BASE_DIR + "modeling_summary.csv"
        df_results = pd.read_csv(model_results_path)

        st.subheader("Modeling Summary Table")
        st.dataframe(df_results)

        metric = st.selectbox("Select Metric to Plot:", ["Accuracy", "F1 Score", "RMSE", "MAE", "R2"])

        if metric in df_results.columns:
            plt.figure(figsize=(12,6))
            sns.barplot(data=df_results[df_results['Status'] == '✅ Modeled'], x='Event', y=metric, hue='Model')
            plt.title(f"{metric} Comparison Across Models")
            plt.xticks(rotation=45)
            plt.grid(True)
            st.pyplot(plt.gcf())
        else:
            st.warning(f"Metric {metric} not available!")

    elif page == "📊 Feature Trends":
        st.title("📊 Feature Trends Over Time")

        scaled_features_path = BASE_DIR + "environmental_features_scaled.csv"
        df_scaled = pd.read_csv(scaled_features_path)

        feature_to_plot = st.selectbox("Select a Feature to Explore:", [col for col in df_scaled.columns if col.startswith('scaled_')])

        plt.figure(figsize=(10,5))
        sns.lineplot(data=df_scaled, x='Year', y=feature_to_plot)
        plt.title(f"Trend of {feature_to_plot}")
        plt.grid(True)
        st.pyplot(plt.gcf())

# Error Handling
else:
    st.warning("⚠️ Please select a valid Domain and Report.")
