
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_agricultural_yield():
    st.subheader("📈 Agricultural Yield Trends in Nepal")

    try:
        df = pd.read_csv("data/Socioeconomic/clean_data/agricultural_yield_clean.csv")
        df['YEAR'] = df['YEAR'].astype(int)

        avg_yield = df.groupby('YEAR')['YIELD'].mean()

        fig, ax = plt.subplots(figsize=(10,6))
        avg_yield.plot(ax=ax, marker='o')
        ax.set_title("Average Agricultural Yield Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("Yield")
        ax.grid(True)

        st.pyplot(fig)
        st.dataframe(df.head(20), use_container_width=True)

    except Exception as e:
        st.error(f"Error loading agricultural yield data: {e}")
