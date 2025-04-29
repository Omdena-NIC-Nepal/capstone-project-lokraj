import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def show_model_summary():
    BASE_DIR = "data/Environmental/processed_combined/"
    engineered_data_path = BASE_DIR + "engineered_features_scaled.csv"

    try:
        df = pd.read_csv(engineered_data_path)

        st.title(" Machine Learning Model Performance Summary (Live)")

        st.subheader(" Available Features")
        st.dataframe(df.head())

        # --- Select Target Variable ---
        target_variable = st.selectbox(
            " Select Target Variable:",
            ["scaled_Forest_Loss_ha", "scaled_Mean_Discharge_m3s", "scaled_Total_Glacial_Lake_Area_km2"]
        )

        # --- Feature and Target Split ---
        feature_cols = [col for col in df.columns if col.startswith('scaled_') and col != target_variable]
        X = df[feature_cols]
        y = df[target_variable]

        # --- Remove rows with NaN in target ---
        valid_rows = ~y.isna()
        X = X[valid_rows]
        y = y[valid_rows]

        st.info(f" Available samples after cleaning: **{len(X)}**")

        # --- Select Model Type ---
        model_choice = st.selectbox(
            " Choose ML Model:",
            ["Random Forest Regressor", "Linear Regression"]
        )

        # --- Decide Train/Test split ---
        MIN_SAMPLES_FOR_SPLIT = 10  # Threshold to split
        small_dataset = len(X) < MIN_SAMPLES_FOR_SPLIT

        if small_dataset:
            st.warning(f" Only {len(X)} samples available. Skipping train/test split — training on full data.")

            if model_choice == "Random Forest Regressor":
                model = RandomForestRegressor(random_state=42)
            else:
                model = LinearRegression()

            model.fit(X, y)
            y_pred = model.predict(X)

            r2 = r2_score(y, y_pred)
            mae = mean_absolute_error(y, y_pred)
            rmse = np.sqrt(mean_squared_error(y, y_pred))

            true_values = y

        else:
            st.success(f" Enough samples! Proceeding with 70% Train / 30% Test split.")

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            if model_choice == "Random Forest Regressor":
                model = RandomForestRegressor(random_state=42)
            else:
                model = LinearRegression()

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))

            true_values = y_test

        # --- Display Metrics ---
        st.subheader(" Model Evaluation Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("R² Score", f"{r2:.3f}")
        col2.metric("MAE", f"{mae:.3f}")
        col3.metric("RMSE", f"{rmse:.3f}")

        # --- Plot True vs Predicted ---
        st.subheader("🔍 True vs Predicted Values")
        plt.figure(figsize=(8, 6))
        plt.scatter(true_values, y_pred, alpha=0.7)
        plt.xlabel("True Values")
        plt.ylabel("Predicted Values")
        plt.title(f"True vs Predicted: {target_variable} ({model_choice})")
        plt.grid(True)
        st.pyplot(plt.gcf())

    except FileNotFoundError:
        st.error(" 'engineered_features_scaled.csv' not found. Please upload or place the file correctly.")
