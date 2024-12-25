import streamlit as st
def tracks():
    st.subheader('Racing Track Information')
    st.write('---')
    st.markdown('**Bahrain-Sakhir Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Bahrain_Circuit.png.transform/9col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Bahrain\n\nLength of Circuit : 5.412 km\n\n First Race : 2004\n\n Number of laps : 57\n\n Lap record : 1:31.447 - De la Rosa (2005)\n\n Most Wins Driver : Lewis Hamilton (5)\n\n Most Wins Constructor : Ferrai (7)</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('**Jeddah Corniche Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Saudi_Arabia_Circuit.png.transform/7col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Saudi Arabia\n\nLength of Circuit : 6.174 km\n\n First Race : 2021\n\n Number of laps : 50\n\n Lap record : 1:30.734 - Lewis Hamilton (2021)\n\n Most Wins Driver : Max Verstappen (2)\n\n Most Wins Constructor : Red Bull (3)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Australia-Melbourne Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Australia_Circuit.png.transform/6col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Australia\n\nLength of Circuit : 5.303 km\n\n First Race : 1996\n\n Number of laps : 58\n\n Lap record : 1:24.125 - M Schumacher (2004)\n\n Most Wins Driver : Michal Schumacher,Lex Davidson (4)\n\n Most Wins Constructor : Ferrai (14)</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('**Suzuka Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Japan_Circuit.png.transform/6col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Japan\n\nLength of Circuit : 5.807 km\n\n First Race : 1987\n\n Number of laps : 53\n\n Lap record : 1:30.983 - Hamilton (2019)\n\n Most Wins Driver : Michal Schumacher (6)\n\n Most Wins Constructor : McLaren (9)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Shanghai International Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/China_Circuit.png.transform/9col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: China\n\nLength of Circuit : 5.451 km\n\n First Race : 2004\n\n Number of laps : 56\n\n Lap record : 1:32.238 - M Schumacher (2004)\n\n Most Wins Driver : Lewis Hamilton (6)\n\n Most Wins Constructor : Mercedes (6)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Miami International Autodrome**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monaco_Circuit" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: United States\n\nLength of Circuit : 5.412 km\n\n First Race : 2022\n\n Number of laps : 57\n\n Lap record : 1:29.708 Max Verstappen (2023)\n\n Most Wins Driver : Max Verstappen (2)\n\n Most Wins Constructor : Red Bull (2)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Autodromo Enzo e Dino Ferrari**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Emilia_Romagna_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Italy\n\nLength of Circuit : 4.909 km\n\n First Race : 1980\n\n Number of laps : 63\n\n Lap record : 1:15.484 Lewis Hamilton (2020)\n\n Most Wins Driver : Max Verstappen (2)\n\n Most Wins Constructor : Red Bull (2)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit de Monaco**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244984/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monoco_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Monaco\n\nLength of Circuit : 3.337 km\n\n First Race : 1950\n\n Number of laps : 78\n\n Lap record : 1:12.909 Lewis Hamilton (2021)\n\n Most Wins Driver : Ayrton Senna (6)\n\n Most Wins Constructor : McLaren (15)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit Gilles-Villeneuve**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Canada_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Canada\n\nLength of Circuit : 4.361 km\n\n First Race : 1978\n\n Number of laps : 70\n\n Lap record : 1:13.078 Valtteri Bottas (2019)\n\n Most Wins Driver : Michael Schumacher, Lewis hamilton (7)\n\n Most Wins Constructor : Ferrari (14)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit de Barcelona-Catalunya**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244986/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Spain_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Spain\n\nLength of Circuit : 4.909 km\n\n First Race : 1980\n\n Number of laps : 63\n\n Lap record : 1:15.484 Lewis Hamilton (2020)\n\n Most Wins Driver : Michael Schumacher, Lewis hamilton (7)\n\n Most Wins Constructor : Ferrai (12)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Red Bull Ring**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Austria_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Austria\n\nLength of Circuit : 4.318 km\n\n First Race : 1970\n\n Number of laps : 71\n\n Lap record : 1:05.619 Carlos Sainz (2020)\n\n Most Wins Driver : Max Verstappen (4)\n\n Most Wins Constructor : Ferrari (7)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Silverstone Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Great_Britain_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Great Britain\n\nLength of Circuit : 5.891 km\n\n First Race : 1950\n\n Number of laps : 52\n\n Lap record : 1:27.097 Max Verstappen (2020)\n\n Most Wins Driver : Lewis Hamilton (8)\n\n Most Wins Constructor : Ferrari (18)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Hungaroring**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Hungary_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Hungary\n\nLength of Circuit : 4.381 km\n\n First Race : 1986\n\n Number of laps : 70\n\n Lap record : 1:16.627 Lewis Hamilton (2020)\n\n Most Wins Driver : Lewis Hamilton (8)\n\n Most Wins Constructor : McLaren (11)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit de Spa-Francorchamps**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Belgium_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Belgian\n\nLength of Circuit : 7.004 km\n\n First Race : 1950\n\n Number of laps : 44\n\n Lap record : 1:46.286 Valtteri Bottas (2018)\n\n Most Wins Driver : Michael Schumacher (6)\n\n Most Wins Constructor : Ferrari (18)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit Zandvoort**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244984/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Netherlands_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Netherlands\n\nLength of Circuit : 4.259 km\n\n First Race : 1952\n\n Number of laps : 72\n\n Lap record : 1:11.097 Lewis Hamilton (2021)\n\n Most Wins Driver : Jim Clark (4)\n\n Most Wins Constructor : Ferrai (8)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Autodromo Nazionale Monza**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244987/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Italy_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Italy\n\nLength of Circuit : 5.793 km\n\n First Race : 1950\n\n Number of laps : 53\n\n Lap record : 1:21.046 Rubens Barrichello (2004)\n\n Most Wins Driver : Michael Schumacher, Lewis hamilton (5)\n\n Most Wins Constructor : Ferrari (20)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Baku City Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244987/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Baku_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Azerbaijan\n\nLength of Circuit : 6.003 km\n\n First Race : 2016\n\n Number of laps : 51\n\n Lap record : 1:43.009 Charles Leclerc (2019)\n\n Most Wins Driver : Sergio Perez (2)\n\n Most Wins Constructor : Red Bull (4)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Marina Bay Street Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1683633963/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Singapore_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Singapore\n\nLength of Circuit : 4.94 km\n\n First Race : 2008\n\n Number of laps : 62\n\n Lap record : 1:35.867 Lewis Hamilton (2019)\n\n Most Wins Driver : Sebastian Vettel (5)\n\n Most Wins Constructor : Ferrari (5)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Circuit of The Americas**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244984/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/USA_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: United States\n\nLength of Circuit : 5.513 km\n\n First Race : 2012\n\n Number of laps : 56\n\n Lap record : 1:36.169 Charles Leclerc (2019)\n\n Most Wins Driver : Lewis Hamilton (6)\n\n Most Wins Constructor : Ferrari (10)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Autódromo Hermanos Rodríguez**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Mexico_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Mexico\n\nLength of Circuit : 4.304 km\n\n First Race : 1963\n\n Number of laps : 71\n\n Lap record : 1:17.774 Valtteri Bottas (2021)\n\n Most Wins Driver : Max Verstappen (5)\n\n Most Wins Constructor : Red Bull (5)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Autódromo José Carlos Pace**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Brazil_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Brazil\n\nLength of Circuit : 4.309 km\n\n First Race : 1973\n\n Number of laps : 71\n\n Lap record : 1:10.540 Valtteri Bottas (2018)\n\n Most Wins Driver : Alain Prost (6)\n\n Most Wins Constructor : McLaren (12)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Las Vegas Strip Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677249930/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Las_Vegas_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: United States\n\nLength of Circuit : 6.201 km\n\n First Race : 2023\n\n Number of laps : 50\n\n Lap record : 1:35.490 Oscar Piastri (2023)\n\n Most Wins Driver : Max Verstappen (1)\n\n Most Wins Constructor : Red Bull (1)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Lusail International Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Qatar_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: Qatar\n\nLength of Circuit : 5.419 km\n\n First Race : 2021\n\n Number of laps : 57\n\n Lap record : 1:24.319 Max Verstappen (2023)\n\n Most Wins Driver : Lewis Hamilton, Max Verstappen (1)\n\n Most Wins Constructor : Mercedes, Red Bull (1)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('**Yas Marina Circuit**')
    st.markdown('<img src="https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Abu_Dhabi_Circuit.png.transform/4col/image.png" width="700" height="400"/>',unsafe_allow_html=True)
    st.write("""
    <div style="background-color: #6D1B07; padding: 2px;">
        <span style="color: white;">\n\n Country: United arab Emirates\n\nLength of Circuit : 5.281 km\n\n First Race : 2009\n\n Number of laps : 58\n\n Lap record : 1:26.103 Max Verstappen (2021)\n\n Most Wins Driver : Lewis Hamilton (5)\n\n Most Wins Constructor : Red Bull (7)</span>
    </div>
    """, unsafe_allow_html=True)
