import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_feature_trends():
    BASE_DIR = "data/Environmental/processed_combined/"
    scaled_features_path = BASE_DIR + "environmental_features_scaled.csv"

    try:
        df_scaled = pd.read_csv(scaled_features_path)

        st.title(" Feature Trends Over Time")

        feature_columns = [col for col in df_scaled.columns if col.startswith('scaled_')]
        if not feature_columns:
            st.warning(" No scaled features found in dataset!")
        else:
            feature_to_plot = st.selectbox("Select a Feature to Explore:", feature_columns)

            sns.set_theme(style="whitegrid")
            plt.figure(figsize=(10, 5))
            sns.lineplot(data=df_scaled, x='Year', y=feature_to_plot)
            plt.title(f"Trend of {feature_to_plot}")
            plt.grid(True)
            st.pyplot(plt.gcf())

    except FileNotFoundError:
        st.error(" 'environmental_features_scaled.csv' not found!")
