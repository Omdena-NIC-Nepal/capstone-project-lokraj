import streamlit as st
import pandas as pd

def show_model_evaluation():
    st.header(" Glacier Model Evaluation")

    # Load model evaluation metrics
    metrics_df = pd.read_csv("data/glacier/ERA5/model_metrics.csv")  # Save your evaluation earlier to this CSV

    st.dataframe(metrics_df)

    st.markdown("""
    **Model Description:**
    - Linear Regression: Assumes linear relationship
    - Ridge Regression: Adds regularization
    - Polynomial Regression: Models non-linearity
    """)
