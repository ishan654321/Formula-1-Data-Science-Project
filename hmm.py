import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from PIL import Image
#st. set_page_config(layout="wide")
img=Image.open(r'D:\F1 track record csv\formula1projectlogo.jfif')
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
}
[data-testid="stVerticalBlock"] {
width: 100%;
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
</style>
"""
st.markdown(sidebar_bg_img,unsafe_allow_html=True)
# Load data for analysis
pit_stop_df = pd.read_csv(r'D:\F1 track record csv\pit_stops_1.csv')
drivers_df = pd.read_csv(r'D:\F1 track record csv\drivers_1.csv')
races_df = pd.read_csv(r'D:\F1 track record csv\races.csv')
lap_time_df=pd.read_csv(r'D:\F1 track record csv\lap_times_1.csv')

# Load data for prediction
data = pd.read_csv(r'D:\F1 track record csv\DriverPrediction.csv')
data_constructor=pd.read_csv(r'D:\F1 track record csv\ConstructorPrediction.csv')
# Function for analysis
def analyze_pitstop_duration():
    # Merge necessary tables
    merged_data = pd.merge(pit_stop_df, drivers_df, on='driverId')
    merged_data = pd.merge(merged_data, races_df, on='raceId')

    st.write("""
    <div style="background-color: #F3DC7A; padding: 10px;">
        <span style="color: black;">Pitstop is a process of changing tyres throughout the race. Tyres can be of 5 types. \n\n  1)Soft Tyres: Turns fast but duration is less.\n\n 2)Medium Tyres: Turns medium faster and duration is more than soft tyres.\n\n 3)Hard Tyres: Turn slower but duration is much more.\n\n 4)Intermediate Tyres: Used on slighly wet track.\n\n 5)Wet Tyres: Used on highly wet track.\n\n Note: Below analysis time includes total duration of entering pitlane to exiting pitlane.</span>
    </div>
    """, unsafe_allow_html=True)

    # Filter data between raceId 1031 and 1047 which is year 2018
    filtered_data2018 = merged_data[(merged_data['raceId'] >= 989) & (merged_data['raceId'] <= 1009)]

    average_pitstop_duration2018 = filtered_data2018.groupby('forename')['milliseconds'].mean().reset_index()
    st.subheader('Analysis: Average Pitstop Duration by Driver (2018)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2018['forename'], average_pitstop_duration2018['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Average Pitstop Duration (seconds)',color='white')
    plt.title('Average Pitstop Duration by Driver (2018)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt,use_container_width=True)

    # Filter data between raceId 1031 and 1047 which is year 2019
    filtered_data2019 = merged_data[(merged_data['raceId'] >= 1010) & (merged_data['raceId'] <= 1030)]

    average_pitstop_duration2019 = filtered_data2019.groupby('forename')['milliseconds'].mean().reset_index()
    st.subheader('Analysis: Average Pitstop Duration by Driver (2019)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2019['forename'], average_pitstop_duration2019['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Average Pitstop Duration (seconds)',color='white')
    plt.title('Average Pitstop Duration by Driver (2019)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt,use_container_width=True)

    # Filter data between raceId 1031 and 1047 which is year 2020
    filtered_data2020 = merged_data[(merged_data['raceId'] >= 1031) & (merged_data['raceId'] <= 1047)]

    average_pitstop_duration2020 = filtered_data2020.groupby('forename')['milliseconds'].mean().reset_index()
    st.subheader('Analysis: Average Pitstop Duration by Driver (2020)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2020['forename'], average_pitstop_duration2020['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Average Pitstop Duration (seconds)',color='white')
    plt.title('Average Pitstop Duration by Driver (2020)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt,use_container_width=True)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Jack Aitken, Nico Hulkenberg, and Pietro Fittipaldi were only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)

    # Filter data between raceId 1051 and 1073 which is year 2021
    filtered_data2021 = merged_data[(merged_data['raceId'] >= 1051) & (merged_data['raceId'] <= 1073)]

    average_pitstop_duration2021 = filtered_data2021.groupby('forename')['milliseconds'].mean().reset_index()
    st.subheader('Analysis: Average Pitstop Duration by Driver (2021)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2021['forename'], average_pitstop_duration2021['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Average Pitstop Duration (seconds)',color='white')
    plt.title('Average Pitstop Duration by Driver (2021)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Robert Kubica was only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)

    # Filter data between raceId 1074 and 1096 which is year 2022
    filtered_data2022 = merged_data[(merged_data['raceId'] >= 1074) & (merged_data['raceId'] <= 1096)]

    average_pitstop_duration2022 = filtered_data2022.groupby('forename')['milliseconds'].mean().reset_index()

    st.subheader('Analysis: Average Pitstop Duration by Driver (2022)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2022['forename'], average_pitstop_duration2022['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Average Pitstop Duration (seconds)',color='white')
    plt.title('Average Pitstop Duration by Driver (2022)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Nyck De Vries and Nico Hulkenberg were only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)

    pitstop_winner_df=pd.read_csv(r'D:\F1 track record csv\DHL_Pitstop_Winners.csv')
    st.subheader('Analysis: DHL Fastest Pitstop Award Winners')
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(pitstop_winner_df['Constructor'], pitstop_winner_df['Win'],color='#E11433')
    plt.xlabel('Year',color='white')
    plt.ylabel('Constructor',color='white')
    plt.title('DHL Pitstop Winners',color='white')
    plt.xticks(rotation=0,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: This award is being awarded since 2015 sponsered by DHL.</span>
    </div>
    """, unsafe_allow_html=True)

def lap_analysis():
    # Merge necessary tables
    merged_data = pd.merge(lap_time_df, drivers_df, on='driverId')
    merged_data = pd.merge(merged_data, races_df, on='raceId')

    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Lap time may differ from race to race and track to track. Some track are shorter while some are longer.</span>
    </div>
    """, unsafe_allow_html=True)
    # Filter data between raceId 989 and 1009 which is year 2018
    filtered_data2018 = merged_data[(merged_data['raceId'] >= 989) & (merged_data['raceId'] <= 1009)]
  
    # Filter data between raceId 1010 and 1030 which is year 2019
    filtered_data2019 = merged_data[(merged_data['raceId'] >= 1010) & (merged_data['raceId'] <= 1030)]

    # Filter data between raceId 1031 and 1047 which is year 2020
    filtered_data2020 = merged_data[(merged_data['raceId'] >= 1031) & (merged_data['raceId'] <= 1047)]
    
    # Filter data between raceId 1051 and 1074 which is year 2021
    filtered_data2021 = merged_data[(merged_data['raceId'] >= 1051) & (merged_data['raceId'] <= 1073)]
    
    # Filter data between raceId 1074 and 1096 which is year 2022
    filtered_data2022 = merged_data[(merged_data['raceId'] >= 1074) & (merged_data['raceId'] <= 1096)]
    
    # Calculate average pit stop duration by driverId
    average_pitstop_duration2018 = filtered_data2018.groupby('forename')['milliseconds'].mean().reset_index()

    average_pitstop_duration2019 = filtered_data2019.groupby('forename')['milliseconds'].mean().reset_index()

    average_pitstop_duration2020 = filtered_data2020.groupby('forename')['milliseconds'].mean().reset_index()

    average_pitstop_duration2021 = filtered_data2021.groupby('forename')['milliseconds'].mean().reset_index()

    average_pitstop_duration2022 = filtered_data2022.groupby('forename')['milliseconds'].mean().reset_index()

    st.subheader('Analysis: Average Laptime Duration by Driver (2018)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2018['forename'], average_pitstop_duration2018['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver Reference',color='white')
    plt.ylabel('Average Lap Duration (seconds)',color='white')
    plt.title('Average Lap Duration by Driver 2018',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)

    st.subheader('Analysis: Average Laptime Duration by Driver (2019)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2019['forename'], average_pitstop_duration2019['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver Reference',color='white')
    plt.ylabel('Average Lap Duration (seconds)',color='white')
    plt.title('Average Lap Duration by Driver 2019',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)
    
    st.subheader('Analysis: Average Laptime Duration by Driver (2020)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2020['forename'], average_pitstop_duration2020['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver Reference',color='white')
    plt.ylabel('Average Lap Duration (seconds)',color='white')
    plt.title('Average Lap Duration by Driver 2020',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Jack Aitken, Nico Hulkenberg, and Pietro Fittipaldi were only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader('Analysis: Average Laptime Duration by Driver (2021)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2021['forename'], average_pitstop_duration2021['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver Reference',color='white')
    plt.ylabel('Average Lap Duration (seconds)',color='white')
    plt.title('Average Lap Duration by Driver 2021',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Robert Kubica was only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader('Analysis: Average Laptime Duration by Driver (2022)')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(average_pitstop_duration2022['forename'], average_pitstop_duration2022['milliseconds']/1000,color='#E11433')
    plt.xlabel('Driver Reference',color='white')
    plt.ylabel('Average Lap Duration (seconds)',color='white')
    plt.title('Average Lap Duration by Driver 2022',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    #plt.grid(True)
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Nyck De Vries and Nico Hulkenberg were only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)
# Function for prediction
def predict_points(data):
    # Selecting relevant features for prediction
    X = data[['driverRating', 'carRating','constructorStrategy' ,'2021_points', '2022_points']]
    y = data['2023_points']

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating and fitting the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predicting on the test set
    predictions = model.predict(X_test)

    # Calculating mean squared error
    mse = mean_squared_error(y_test, predictions)

    # Predicting 2024 points for all drivers
    predicted_2024_points = model.predict(X)

    # Adding predicted points to the dataframe
    data['predicted_2024_points'] = predicted_2024_points
    data['predicted_2024_points'] = data['predicted_2024_points'].round().clip(lower=0)
    data=data.sort_values(by=['predicted_2024_points'],ascending=False)

    # Displaying the results
    st.write("Mean Squared Error:", mse)
    data_to_show = data[['driverRef','2021_points', '2022_points', '2023_points', 'predicted_2024_points']].to_html(index=False)
    styled_html = f'<div style="background-color:black; color:white; padding:10px">{data_to_show}</div>'
    st.write(styled_html, unsafe_allow_html=True)
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    bars=plt.bar(data['driverRef'], data['predicted_2024_points'], color='#E11433')
    plt.xlabel('Driver',color='white')
    plt.ylabel('Predicted 2024 Points',color='white')
    plt.title('Predicted 2024 Points for Each Driver',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    plt.tight_layout()

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval, round(yval, 2), va='bottom',color='white')
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Predicting sports results are not always accurate. I have used linear regression model to predict the data with the use of last 3 years of points data, driver skill rating, car rating and constructor strategy.</span>
    </div>
    """, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------
    st.write('---------------------------------------------------------------------------------------')
    data_to_show2 = data_constructor[['Constructor','2021_Points','2022_Points','2023_Points','Predicted_2024_Points']].to_html(index=False)
    styled_html2 = f'<div style="background-color:black; color:white; padding:10px">{data_to_show2}</div>'
    st.write(styled_html2, unsafe_allow_html=True)
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    bars=plt.bar(data_constructor['Constructor'], data_constructor['Predicted_2024_Points'], color='#E11433')
    plt.xlabel('Constructor',color='white')
    plt.ylabel('Predicted 2024 Points',color='white')
    plt.title('Predicted 2024 Points for Constructor',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    plt.tight_layout()

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x()+ bar.get_width()/3, yval, round(yval, 2), va='bottom',color='white')
    
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: This data is based on drivers prediction.\n\n -- AlphaTauri is renamed as Racing Bulls.</span>
    </div>
    """, unsafe_allow_html=True)
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
def plot_pie_chart_point(constructor_data, title):
    # Filter out rows with points less than 100
    top_constructors = constructor_data[constructor_data['Points'] >= 160]
    other_row = pd.DataFrame(data={
        'Constructor': ['Other'],
        'Points': [constructor_data[constructor_data['Points'] < 160]['Points'].sum()]
    })
    combined_data = pd.concat([top_constructors, other_row])

    # Create labels with constructor names and points counts
    labels = [f"{constructor} ({points})" for constructor, points in zip(combined_data['Constructor'], combined_data['Points'])]

    # Plot the pie chart with a black background and equal size
    with plt.style.context({'axes.facecolor': 'black', 'figure.facecolor': '#F3DC7A'}):
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(combined_data['Points'], labels=labels, textprops={'color': 'black'})
        # Add a border around the pie chart
        ax.add_artist(plt.Circle((0, 0), 1.0, edgecolor='black', linewidth=2, fill=False))
        ax.set_title(title)
        st.pyplot(fig)

def plot_pie_chart_wins(constructor_data, title):
    # Filter out rows with podium counts equal to 0
    combined_data = constructor_data[constructor_data['wins'] > 0]

    # Create labels with constructor names and win counts
    labels = [f"{constructor} ({wins})" for constructor, wins in zip(combined_data['Constructor'], combined_data['wins'])]

    # Plot the pie chart with a black background
    with plt.style.context({'axes.facecolor': 'black', 'figure.facecolor': '#F3DC7A'}):
        plt.figure(figsize=(2, 2))
        plt.pie(combined_data['wins'], labels=labels, textprops={'color': 'black'})
        # Add a border around the pie chart
        plt.gca().add_artist(plt.Circle((0, 0), 1.0, edgecolor='black', linewidth=2, fill=False))
        plt.title(title)
        st.pyplot(plt)
def plot_pie_chart_podium(constructor_data, title):
    # Filter out rows with podium counts equal to 0
    combined_data = constructor_data[constructor_data['podium'] > 1]

    # Create labels with constructor names and podium counts
    labels = [f"{constructor} ({podium})" for constructor, podium in zip(combined_data['Constructor'], combined_data['podium'])]

    # Plot the pie chart with a black background
    with plt.style.context({'axes.facecolor': 'black', 'figure.facecolor': '#F3DC7A'}):
        plt.figure(figsize=(2, 2))
        plt.pie(combined_data['podium'], labels=labels, textprops={'color': 'black'})
        # Add a border around the pie chart
        plt.gca().add_artist(plt.Circle((0, 0), 1.0, edgecolor='black', linewidth=2, fill=False))
        plt.title(title)
        st.pyplot(plt)

def constructor_analysis():
    # Read the constructor standings data for 2023 and 2022
    constructor_2023 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2023.csv')
    constructor_2022 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2022.csv')
    constructor_2021 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2021.csv')

    # Display the subheaders
    st.subheader('Constructor Standings 2022 vs 2021 for Podium')

    # Display pie charts side by side in one row
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart_podium(constructor_2023, "Constructor Standings (2023)")
    with col2:
        plot_pie_chart_podium(constructor_2022, "Constructor Standings (2022)")
    with col3:
        plot_pie_chart_podium(constructor_2021, "Constructor Standings (2021)")

    # Display the subheaders
    st.subheader('Constructor Standings 2022 vs 2021 for Wins')

    # Display pie charts side by side in one row
    col1,col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart_wins(constructor_2023, "Constructor Standings (2023)")
    with col2:
        plot_pie_chart_wins(constructor_2022, "Constructor Standings (2022)")
    with col3:
        plot_pie_chart_wins(constructor_2021, "Constructor Standings (2021)")
    # Display the subheaders
    st.subheader('Constructor Standings 2022 vs 2021 for Points')

    # Display pie charts side by side in one row
    col1,col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart_point(constructor_2023, "Constructor Standings (2023)")
    with col2:
        plot_pie_chart_point(constructor_2022, "Constructor Standings (2022)")
    with col3:
        plot_pie_chart_point(constructor_2021, "Constructor Standings (2021)")
  
    consTitle_df=pd.read_csv(r'D:\F1 track record csv\Constructor_Titles.csv')
     # Create labels with constructor names and podium counts
    labels = [f"{Constructor} ({Titles})" for Constructor, Titles in zip(consTitle_df['Constructor'], consTitle_df['Titles'])]
    with plt.style.context({'axes.facecolor': 'black', 'figure.facecolor': '#F3DC7A'}):
        # For Constructor Titles
        st.subheader("Most Successful Constructors")
        plt.figure(figsize=(5,5))
        plt.pie(consTitle_df['Titles'],labels=labels,textprops={'color':'black'})
        plt.gca().add_artist(plt.Circle((0, 0), 1.0, edgecolor='black', linewidth=2, fill=False))
        st.pyplot(plt)

# Streamlit UI
st.markdown("""
    <h1 style='color: red; font-size: 46px;'>🏎️F1 Analysis and Predictions🏎️</h1>
""", unsafe_allow_html=True)


# Sidebar layout for buttons
with st.sidebar:
    st.header('Navigation')
    analysis_button = st.button("Pitstop Analysis")
    prediction_button = st.button("Prediction")
    lap_analysis_button=st.button("Laptime Analysis")
    tableau_viz_button=st.button('Tableau Dashboard')
    constructor_button=st.button('Constructor Analysis')

# Show analysis or prediction based on button click
if analysis_button:
    analyze_pitstop_duration()
if lap_analysis_button:
    lap_analysis()
if prediction_button:
    st.header('Prediction: F1 Driver Points for 2024 Season')
    predict_points(data)
if tableau_viz_button:
    tableau_viz()
if constructor_button:
    constructor_analysis()