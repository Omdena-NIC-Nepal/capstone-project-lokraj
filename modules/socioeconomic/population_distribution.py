import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

def show_population_distribution():
    st.subheader(" Population Distribution Across Nepal Districts")

    try:
        # Correct relative path
        df = pd.read_csv("data/Socioeconomic/clean_data/population_data_clean.csv")

        # Show the full table
        st.dataframe(df, use_container_width=True)

      
        top_districts = df.sort_values("Total Population", ascending=False)

        # Plot top 10
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(top_districts["Districts"], top_districts["Total Population"], color='skyblue')
        ax.set_title("Districts by Total Population (2011 Census)")
        ax.set_xlabel("District")
        ax.set_ylabel("Total Population")
        ax.set_xticklabels(top_districts["Districts"], rotation=45, ha='right')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading population distribution data: {e}")
