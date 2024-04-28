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
# Boolean variable to track button click
button_clicked = False

# Load data for prediction
data = pd.read_csv(r'DriverPrediction.csv')
# Sidebar layout for buttons
with st.sidebar:
    st.header('Navigation')
    about_button=st.button('About Formula 1')
    tracks_button=st.button('Track Information')
    prediction_button = st.button("Prediction")
    drivers_button=st.button("Drivers")
    analysis_button = st.button("Pitstop & Laptime Analysis")
    tableau_viz_button=st.button('Tableau Dashboard')
    constructor_button=st.button('Constructor Analysis')
    historical_button=st.button('Historical Analysis')
    yearlyanalysis_button=st.button('2023 Analysis')
    references_button=st.button('References')

# Show result based on button click
if analysis_button:
    button_clicked = True
    st.button("Back to Home")
    analyze_pitstop_duration()
    lap_analysis()
elif tracks_button:
    button_clicked = True
    st.button("Back to Home")
    tracks()
elif prediction_button:
    button_clicked = True
    st.button("Back to Home")
    predict_points(data)
elif tableau_viz_button:
    button_clicked = True
    st.button("Back to Home")
    tableau_viz()
elif constructor_button:
    button_clicked = True
    st.button("Back to Home")
    constructor_analysis()
elif historical_button:
    button_clicked = True
    st.button("Back to Home")
    historical()
elif drivers_button:
    button_clicked = True
    st.button("Back to Home")
    drivers()
elif yearlyanalysis_button:
    button_clicked=True
    st.button("Back to Home")
    yearanalysis()
elif about_button:
    button_clicked=True
    st.button("Back To Home")
    about()
elif references_button:
    button_clicked=True
    st.button("Back To Home")
    references()

# If no button is clicked, display home page content
if not button_clicked:

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
            <a href="#upcoming-races" style="text-decoration: none;"><button style="background-color: #6D1B07; color: white; padding: 10px 20px; margin: 10px; border: none; border-radius: 5px;">Upcoming Races</button></a>
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

    # Section for Upcoming Races
    st.write("""
        <div id="upcoming-races" style="padding: 20px; ">
            <h2>Upcoming Races</h2>
            <p>Don't miss out on the excitement! Check out the schedule for upcoming Formula 1 races:</p>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Miami GP</strong><br>
                    3-5 May
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Emilia-Romagna GP</strong><br>
                    17-19 May
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Monaco GP</strong><br>
                    24-26 May
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Canada GP</strong><br>
                    7-9 June
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Spain GP</strong><br>
                    21-23 June
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Austria GP</strong><br>
                    28-30 June
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>British GP</strong><br>
                    5-7 July
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Hungary GP</strong><br>
                    19-21 July
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Belgium GP</strong><br>
                    26-28 July
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Netherlands GP</strong><br>
                    23-25 August
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Italy GP</strong><br>
                    30-1 Aug/Sep
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Azerbaijan GP</strong><br>
                    13-15 September
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Singapore GP</strong><br>
                    20-22 September
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>US GP</strong><br>
                    18-20 October
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Mexico GP</strong><br>
                    25-27 October
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Brazil GP</strong><br>
                    1-3 November
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Las Vegas GP</strong><br>
                    21-23 November
                </div>
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Qatar GP</strong><br>
                    29-1 Nov/Dec
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap;background-color: #000000;">
                <div style="flex: 0 0 33.33%; padding: 10px;">
                    <strong>Abu Dhabi GP</strong><br>
                    6-8 December
                </div>
            </div>
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
