import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tableau_viz():
    st.subheader('Tableau Visualization Constructor Dashboard')

    embedded_code = """
    <iframe src="https://public.tableau.com/views/F1Analysis_17030682058580/Dashboard1?:showVizHome=no&:embed=true" 
    width="800" 
    height="600">
    </iframe>
    """
    st.components.v1.html(embedded_code, width=820, height=620)
    st.subheader('Tableau Visualization Driver Dashboard')

    embedded_code2 = """
    <iframe src="https://public.tableau.com/shared/2MK69P83C?:showVizHome=no&:embed=true" 
    width="1100" 
    height="600">
    </iframe>
    """
    st.components.v1.html(embedded_code2, width=820, height=620)
