import streamlit as st

def show_about_environment():
    st.title(" About the Environment Module")

    st.markdown("""
    ### Module Overview
    This section provides analysis of Nepal's critical environmental indicators:
    -  Forest cover change and deforestation trends
    -  Glacier formation and melting trends
    -  Water resource health, river discharge and water quality

    ### Data Sources
    - Ministry of Forests and Environment, Nepal
    - Department of Hydrology and Meteorology (DHM)
    - Satellite-derived datasets

    ### Purpose
    This analysis helps to:
    - Track environmental degradation or improvement
    - Support conservation initiatives
    - Guide policymaking for sustainable development
    """)
