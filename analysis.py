import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data for analysis
pit_stop_df = pd.read_csv(r'pit_stops_1.csv')
drivers_df = pd.read_csv(r'drivers_1.csv')
races_df = pd.read_csv(r'races.csv')
lap_time_df=pd.read_csv(r'lap_times_1.csv')

def analyze_pitstop_duration():
    # Merge necessary tables
    merged_data = pd.merge(pit_stop_df, drivers_df, on='driverId')
    merged_data = pd.merge(merged_data, races_df, on='raceId')

    st.write("""
    <div style="background-color: #6D1B07; padding: 10px;">
        <span style="color: white;">\n\nPitstop is a process of changing tyres throughout the race. Tyres can be of 5 types. \n\n  1. Soft Tyres: Turns fast but duration is less.\n\n 2. Medium Tyres: Turns medium faster and duration is more than soft tyres.\n\n 3. Hard Tyres: Turn slower but duration is much more.\n\n 4. Intermediate Tyres: Used on slighly wet track.\n\n 5. Wet Tyres: Used on highly wet track.\n\n Note: Below analysis time includes total duration of entering pitlane to exiting pitlane.</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<img src="https://i.redd.it/vix52hlstvc81.gif" width="700" height="360"/>', unsafe_allow_html=True)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: This award is being awarded since 2015 sponsered by DHL.</span>
    </div>
    """, unsafe_allow_html=True)

#-----------------------------------------------------------------------------------------------------------
# Load data for analysis
pit_stop_df = pd.read_csv(r'D:\F1 track record csv\pit_stops_1.csv')
drivers_df = pd.read_csv(r'D:\F1 track record csv\drivers_1.csv')
races_df = pd.read_csv(r'D:\F1 track record csv\races.csv')
lap_time_df=pd.read_csv(r'D:\F1 track record csv\lap_times_1.csv')

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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)
    st.write("""
    <div style="background-color: black; padding: 10px;">
        <span style="color: white;">Note: Nyck De Vries and Nico Hulkenberg were only part of a few races.</span>
    </div>
    """, unsafe_allow_html=True)
