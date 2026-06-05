import streamlit as st
from analysis import analyze_pitstop_duration, lap_analysis
from prediction import predict_points
from visualization import tableau_viz
from constructor_analysis import constructor_analysis
from Historical import historical
from TrackInfo import tracks
import pandas as pd
from PIL import Image
from drivers_analysis import drivers
from yearanalysis import yearanalysis
from About import about
from references import references

#st.set_page_config(layout="wide")

img=Image.open(r'formula1projectlogo.jfif')
st.set_page_config(page_title='Formula 1 Data Science',page_icon=img)

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://i.pinimg.com/originals/a4/91/f1/a491f117978c71157ea5fc4f06adbb83.jpg");
background-size: 100%;
}
[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
sidebar_bg_img="""
<style>
[data-testid="stSidebar"]{
color: rgb(0, 0, 0);
background-color: rgb(219, 68, 57)
}
[data-testid="stApp"]{
color: rgb(256,256,256);
}
[data-testid="StyledLinkIconContainer"]{
color: rgb(256,256,256);
}
[data-testid="baseButton-secondary"]{
color: rgb(0,0,0)  
background-color: rgb(255,255,255)
}
[data-testid="collapsedControl"]{
color: rgb(255,255,255)
}
</style>
"""
st.markdown(sidebar_bg_img,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Streamlit UI
st.markdown("""
    <h1 style='color: red; font-size: 46px;'>🏎️F1 Analysis and Predictions🏎️</h1>
""", unsafe_allow_html=True)



def set_page(page_name):
    st.session_state["page"] = page_name

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

with st.sidebar:
    st.header('Navigation')
    st.button('Home', on_click=set_page, args=("Home",))
    st.button('About Formula 1', on_click=set_page, args=("About Formula 1",))
    st.button('Track Information', on_click=set_page, args=("Track Information",))
    st.button("Prediction", on_click=set_page, args=("Prediction",))
    st.button("Drivers", on_click=set_page, args=("Drivers",))
    st.button("Pitstop & Laptime Analysis", on_click=set_page, args=("Pitstop & Laptime Analysis",))
    st.button('Tableau Dashboard', on_click=set_page, args=("Tableau Dashboard",))
    st.button('Constructor Analysis', on_click=set_page, args=("Constructor Analysis",))
    st.button('Historical Analysis', on_click=set_page, args=("Historical Analysis",))
    st.button('2023 Analysis', on_click=set_page, args=("2023 Analysis",))
    st.button('References', on_click=set_page, args=("References",))

page = st.session_state["page"]

if page == "Pitstop & Laptime Analysis":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    analyze_pitstop_duration()
    lap_analysis()

elif page == "Track Information":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    tracks()

elif page == "Prediction":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    data = pd.read_csv("DriverPrediction.csv")
    predict_points(data.copy())

elif page == "Tableau Dashboard":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    tableau_viz()

elif page == "Constructor Analysis":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    constructor_analysis()

elif page == "Historical Analysis":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    historical()

elif page == "Drivers":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    drivers()

elif page == "2023 Analysis":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    yearanalysis()

elif page == "About Formula 1":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    about()

elif page == "References":
    st.button("Back to Home", on_click=set_page, args=("Home",))
    references()

# If no button is clicked, display home page content
if page == "Home":
    # Header section with enhanced styling
    st.write("""
        <div style="background-color: #6D1B07; padding: 20px;">
            <h1 style="color: white; text-align: center;">Formula 1 Insights</h1>
            <p style="color: white; text-align: center; font-size: 18px;">Get analysis and predictions for Formula 1 racing!</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content section with description and buttons
    st.write("""
        <div style="padding: 20px;">
            <h2>About This Project</h2>
            <p style="background-color: #000000; color: #ffffff;">Welcome to my Formula 1 website! Here, you'll find in-depth analysis, predictions, and all the latest news from the world of Formula 1 racing.</p>
            <p style="background-color: #000000; color: #ffffff;">Whether you're a die-hard fan or just getting started, we've got you covered with insights into races, drivers, teams, and more.</p>
            <p style="background-color: #000000; color: #ffffff;">Note: This website contains content taken from various sources including <a href="https://www.formula1.com/" target="_blank">official formula 1 website</a>. I am also declaring that I have used this data and content only for project purpose and not for any commercial or profit reason. All the copyright goes to respective owners of data, images and other contents.</p>
        </div>
        """, unsafe_allow_html=True)

    # Button section for different topics
    st.write("""
        <div style="text-align: center;">
            <h3>Explore Our Insights:</h3>
            <a href="#latest-news" style="text-decoration: none;"><button style="background-color: #6D1B07; color: white; padding: 10px 20px; margin: 10px; border: none; border-radius: 5px;">Latest News</button></a>
            <a href="#driver-standings" style="text-decoration: none;"><button style="background-color: #6D1B07; color: white; padding: 10px 20px; margin: 10px; border: none; border-radius: 5px;">Driver Standings</button></a>
            <a href="#team-standings" style="text-decoration: none;"><button style="background-color: #6D1B07; color: white; padding: 10px 20px; margin: 10px; border: none; border-radius: 5px;">Team Standings</button></a>
        </div>
        """, unsafe_allow_html=True)

    # Section for Latest News
    st.write("""
        <div id="latest-news" style="padding: 20px;">
            <h2>Latest News</h2>
            <p style="background-color: #000000; color: #ffffff;">Stay updated with the most recent news and developments in the world of Formula 1 racing.</p>
            <p style="background-color: #000000; color: #ffffff;">For the latest news, visit <a href="https://www.formula1.com/en/latest/all" target="_blank">Formula1.com</a>.</p>
        </div>
        """, unsafe_allow_html=True)

    standings_df=pd.read_csv(r'CurrentStanding.csv')
    # Section for Driver Standings
    st.write("""
        <div id="driver-standings" style="padding: 20px;">
            <h2>Driver Standings</h2>
            <p>See where your favorite drivers rank in the current Formula 1 championship standings.</p>
            <!-- Add dynamic content here -->
        </div>
        """, unsafe_allow_html=True)
    data_to_show3 = standings_df[['Position','Driver', 'Points']].to_html(index=False, classes='dataframe',border=0)
    styled_html3 = f'<style>table.dataframe{{background-color:black; color:white; padding:10px;}}</style>{data_to_show3}'
    st.write(styled_html3, unsafe_allow_html=True)

    standings_df2=pd.read_csv(r'CurrentStanding2.csv')

    # Section for Team Standings
    st.write("""
        <div id="team-standings" style="padding: 20px;">
            <h2>Team Standings</h2>
            <p>Discover how Formula 1 teams are performing in the championship standings.</p>
        </div>
        """, unsafe_allow_html=True)
    data_to_show4 = standings_df2[['Position','Constructor', 'Points']].to_html(index=False, classes='dataframe',border=0)
    styled_html4 = f'<style>table.dataframe{{background-color:black; color:white; padding:10px;}}</style>{data_to_show4}'
    st.write(styled_html4, unsafe_allow_html=True)
