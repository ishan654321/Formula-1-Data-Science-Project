import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
# Load data for analysis
pit_stop_df = pd.read_csv(r'D:\F1 track record csv\pit_stops_1.csv')
drivers_df = pd.read_csv(r'D:\F1 track record csv\drivers_1.csv')
races_df = pd.read_csv(r'D:\F1 track record csv\races.csv')
lap_time_df=pd.read_csv(r'D:\F1 track record csv\lap_times_1.csv')

# Merge necessary tables
merged_data = pd.merge(pit_stop_df, drivers_df, on='driverId')
merged_data = pd.merge(merged_data, races_df, on='raceId')

filtered_data2018 = merged_data[(merged_data['raceId'] >= 989) & (merged_data['raceId'] <= 1009)]

average_pitstop_duration2018 = filtered_data2018.groupby('forename')['milliseconds'].mean().reset_index()

st.subheader('Analysis: Average Pitstop Duration by Driver (2018)')

# Plotting
plt.figure(figsize=(10, 6), facecolor='#463F41')
ax = plt.axes()
ax.set_facecolor("#463F41")

# Using seaborn color palette for better colors
colors = sns.color_palette('dark:salmon_r', len(average_pitstop_duration2018))

# Plotting the bar chart with seaborn
sns.barplot(x='forename', y='milliseconds', data=average_pitstop_duration2018, palette=colors)
plt.xlabel('Driver name', color='white', fontsize=12)
plt.ylabel('Average Pitstop Duration (milliseconds)', color='white', fontsize=12)
plt.title('Average Pitstop Duration by Driver (2018)', color='white', fontsize=14)
plt.xticks(rotation=90, color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)

# Add data labels
for i, val in enumerate(average_pitstop_duration2018['milliseconds']):
    plt.text(i, val + 1000, round(val/1000, 2), color='white', ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(plt, use_container_width=True)
