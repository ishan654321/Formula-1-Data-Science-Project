import streamlit as st
def references():
    st.subheader('References')
    st.write("""
            <div style="background-color: #FFFFFF; padding: 10px;">
                <span style="color: black;">\n\nI hae used various data sources including <a href="https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020" target="_blank">this</a> kaggle dataset. It was the main source of data. I have also used directly or indirectly <a href="https://www.formula1.com/" target="_blank">Formula 1</a> official webiste data available online. Apart from this I have used multiple free available images from online sources and I hope I will not get copyright strike.</span>
            </div>
            """, unsafe_allow_html=True)
    st.subheader('Technology')
    st.write("""
            <div style="background-color: #FFFFFF; padding: 10px;">
                <span style="color: black;">\n\nI have used below technology stack.\n\n- Python (3.10.2)\n- Streamlit (1.33.0)\n- VSCode\n- Jupyte Notebook\n- Tableau Public\n- Libraries: Pandas, NumPy, Matplotlib, Plotly, PIL, Math.</span>
            </div>
            """, unsafe_allow_html=True)