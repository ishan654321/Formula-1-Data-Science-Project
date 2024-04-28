import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

    st.subheader('Constructors')

    st.markdown('**Oracle Red Bull**')
    st.markdown('<img src="https://www.amalgamcollection.com/cdn/shop/articles/RB18_GIF_b5e81ee8-5e20-4dc6-a1d1-efedd2fc9128_1024x1024.gif?v=1686043650" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 2005\n\nEngine : Honda\n\nTyres : Pirelli\n\nRace wins : 116\n\nChampionship wins: 6</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Scuderia Ferrari**')
    st.markdown('<img src="https://www.amalgamcollection.com/cdn/shop/articles/F1-75_Monza_GIF_UPDATED_1024x1024.gif?v=1680252768" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1950\n\nEngine : Ferrari\n\nTyres : Pirelli\n\nRace wins : 243\n\nChampionship wins: 16</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Mercedes-AMG Petronas**')
    st.markdown('<img src="https://www.amalgamcollection.com/cdn/shop/articles/W13_Mailshot_GIF_1024x1024.gif?v=1688655987" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1954\n\nEngine : Mercedes\n\nTyres : Pirelli\n\nRace wins : 125\n\nChampionship wins: 8</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**McLaren**')
    st.markdown('<img src="https://i.pinimg.com/originals/c0/c7/79/c0c779295f1cf2bcebde0939fc29a51c.gif" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1966\n\nEngine : Mercedes\n\nTyres : Pirelli\n\nRace wins : 183\n\nChampionship wins: 8</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Aston Martin Aramaco**')
    st.markdown('<img src="https://www.team-bhp.com/forum/attachments/intl-motorsport/2128163d1614786698-aston-martin-f1-car-amr21-revealed-238b2322cba743afbde10862e6d8effe.jpeg" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1959\n\nEngine : Mercedes\n\nTyres : Pirelli\n\nRace wins : 0\n\nChampionship wins: 0</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Money Gram Haas**')
    st.markdown('<img src="https://www.formula1.com/fom-website/2023/Haas/VF24-NH_4.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 2016\n\nEngine : Ferrari\n\nTyres : Pirelli\n\nRace wins : 0\n\nChampionship wins: 0</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**BWT Alpine**')
    st.markdown('<img src="https://cdn-1.motorsport.com/images/amp/2Gzbp7r0/s1000/alpine-a524.jpg" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 2021\n\nEngine : Renault\n\nTyres : Pirelli\n\nRace wins : 1\n\nChampionship wins: 0</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Visa Cash App RB**')
    st.markdown('<img src="https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cdni.autocarindia.com/ExtraImages/20240209011803_Visa_Cash_App_RB_VCARB_01_front.jpg&w=700&c=1" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 2024\n\nEngine : Honda\n\nTyres : Pirelli\n\nRace wins : 0\n\nChampionship wins: 0</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Williams**')
    st.markdown('<img src="https://cdn.motorsport.com/images/mgl/254WG4E0/s1000/williams-racing-fw46.jpg" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1977\n\nEngine : Mercedes\n\nTyres : Pirelli\n\nRace wins : 114\n\nChampionship wins: 9</span>
    </div>
    """, unsafe_allow_html=True)
   
    st.markdown('**Kick Sauber**')
    st.markdown('<img src="https://media.formula1.com/image/upload/t_16by9Centre/f_auto/q_auto/v1707158152/fom-website/2023/Kick%20Sauber/C44_Front-high_Stake_ZHO_16-9.jpg" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Started since : 1993\n\nEngine : Ferrari\n\nTyres : Pirelli\n\nRace wins : 1\n\nChampionship wins: 0</span>
    </div>
    """, unsafe_allow_html=True)

    # Read the constructor standings data for 2023 and 2022
    constructor_2023 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2023.csv')
    constructor_2022 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2022.csv')
    constructor_2021 = pd.read_csv(r'D:\F1 track record csv\Constructor_Championship_2021.csv')

    # Display the subheaders
    st.subheader('Constructor Standings 2023 vs 2022 vs 2021 for Podium')

    # Display pie charts side by side in one row
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart_podium(constructor_2023, "Constructor Standings (2023)")
    with col2:
        plot_pie_chart_podium(constructor_2022, "Constructor Standings (2022)")
    with col3:
        plot_pie_chart_podium(constructor_2021, "Constructor Standings (2021)")

    # Display the subheaders
    st.subheader('Constructor Standings 2023 vs 2022 vs 2021 for Wins')

    # Display pie charts side by side in one row
    col1,col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart_wins(constructor_2023, "Constructor Standings (2023)")
    with col2:
        plot_pie_chart_wins(constructor_2022, "Constructor Standings (2022)")
    with col3:
        plot_pie_chart_wins(constructor_2021, "Constructor Standings (2021)")
    # Display the subheaders
    st.subheader('Constructor Standings 2023 vs 2022 vs 2021 for Points')

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
