import streamlit as st
def about():
    
    st.subheader('Sensors')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nFormula 1 car contains lots of amazing technologies. For an instance they put nearly <b>300 sensors</b> to get live data from various parts of the to collect data related to <b>temperature, pressure, speed, torque, inertia, displacement</b> and many more. This sensors are connected through <b>analog</b> or <b>ECU</b> (Electronic Control Unit) or network buses. This data can be in form of video, audio, images and bytes of other data. Generally total data collected throughout the weekend is in terabytes but the important data which is actually around <b>30 megabytes</b> and after finishing the race it can be up to <b>60 megabytes</b>. This sensors and multiple equipments which are needed are not available elsewhere it is made by them according to their requirements. </span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<img src="https://media.licdn.com/dms/image/D4D12AQGysyH266dWfg/article-inline_image-shrink_1000_1488/0/1705143651319?e=1718841600&v=beta&t=2OilZhCqP-z8WFrM_Kgen4GcwW8mFSVoJhVhGzO_PNM" width="700" height="370"/>',unsafe_allow_html=True)
    
    st.subheader('Steering')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nThe Formula 1 steering wheel is a sophisticated control hub for the driver, featuring buttons for <b>gear shifts, engine modes</b> and other settings. It includes a display for crucial data, a <b>quick-release mechanism </b>for pit stops, and is customized to each driver's preferences. Modern wheels incorporate <b>LED shift lights</b> and <b>haptic feedback</b> for enhanced performance. <b>Telemetry system</b> is used for tracking the movements of steering.</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<img src="https://www.ontheroadtrends.com/wp-content/uploads/2021/02/volante-F1-TW-ENG.jpg" width="700" height="370"/>',unsafe_allow_html=True)
    
    st.subheader('Telemetry')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nTelemetry analysis is very crucial for teams and drivers. It is a <b>wireless transmission</b> of data to the team from the sensors of the car. This telemetry shows 6 different values concurrently. First is <b>speed</b>, second is <b>RPM</b>, third is <b>Throttle</b>, fourth is <b>brake</b>, fifth is <b>DRS</b> an sometimes their comparison with driver around as a sixth component. This order will be different for different teams. Total length of telemetry on x-axis shows the <b>length of the track.</b> </span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<img src="https://miro.medium.com/v2/resize:fit:2000/1*4iys-zDXVIWoeiLOsLovfw.png" width="700" height="560"/>',unsafe_allow_html=True)
    
    st.subheader('Flags')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nThere are multiple flags which are used in formula 1 however 4 flags are commonly used.\n\n 1. <b>Red flag:</b> It is used to halt a race due to dangerous conditions on the track, such as severe accidents, adverse weather, or debris, ensuring the safety of drivers and track personnel.\n\n2. <b>Yellow flag:</b> A yellow flag in Formula 1 is used to warn drivers of a hazard on the track, such as a crash, debris, or adverse conditions, prompting them to slow down and proceed with caution to ensure safety.\n\n3. <b>Green flag:</b> A green flag in Formula 1 indicates the track is clear and safe for racing after a caution period or incident, signaling drivers to resume full-speed racing.\n\n4. <b>Checkered flag:</b> The checkered flag in Formula 1 is waved at the end of a race to signal its completion, indicating the winner and prompting all drivers to finish their final lap.</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<img src="https://d3cm515ijfiu6w.cloudfront.net/wp-content/uploads/2022/05/04141242/Chequered-flag-waved-at-Red-Bull-Ring-Austria-2020-planetf1.jpg" width="700" height="370"/>',unsafe_allow_html=True)
    
    st.subheader('Safty (Halo)')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nIn Formula 1, the halo is a <b>safety device</b> designed to protect drivers' heads from debris and impacts during crashes. It is a curved, <b>titanium structure</b> that surrounds the cockpit of the car, rising above the driver's head. The halo was introduced in <b>2018</b> after extensive research and testing to improve driver safety following several high-profile accidents. While initially met with some skepticism, it has proven effective in numerous incidents, deflecting large debris away from drivers and providing additional protection in the event of a rollover or impact with barriers.</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<img src="https://i.ytimg.com/vi/3-3gIAkYEX8/maxresdefault.jpg" width="700" height="370"/>',unsafe_allow_html=True)
    
    st.subheader('DRS (Drag Reduction System)')
    st.write("""
        <div style="background-color: #FFFFFF; padding: 10px;">
            <span style="color: black;">\n\nThe Drag Reduction System (DRS) in Formula 1 is a movable rear wing system that reduces <b>aerodynamic drag</b> on the car, activated by drivers in <b>designated zones</b> to aid overtaking by <b>increasing straight-line speed</b>. DRS can be enabled when the distance from ahead car is <b>less than 1 second</b>. DRS enable button can be found on steering.</span>
        </div>
        """, unsafe_allow_html=True)
    
