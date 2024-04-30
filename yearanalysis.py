import streamlit as st
import plotly.graph_objects as go
def yearanalysis():
    race_loc=['Bahrain','Saudi Arabia','Australia','Azerbaijan','Miami', 'Monaco','Spanish','Canadian','Austria', 'British','Hungarian','Belgian','Dutch','Italian','Singapore','Japanese','Qatar','United States','Mexican','Brazilian','Las Vegas','Abu Dhabi']
    max_v=[25,44,69,93,119,144,170,195,229,255,281,314,339,364,374,400,433,466,491,524,549,575]
    perez=[18,43,54,87,105,105,117,126,148,156,171,189,201,219,223,223,224,240,240,258,273,285]
    lewis=[10,20,38,48,56,69,87,102,106,121,133,148,156,164,180,190,194,201,220,226,232,234]
    alonso=[15,30,45,60,75,93,99,117,131,137,139,149,168,170,170,174,183,183,183,198,200,206]
    charles=[0,6,6,28,34,42,42,54,72,74,80,99,99,111,123,135,145,151,166,170,188,206]
    norris=[0,0,8,10,10,12,12,12,24,42,60,69,75,79,97,115,136,159,169,195,195,205]
    sainz=[12,20,20,34,44,48,58,68,82,83,87,92,102,117,142,150,153,171,183,192,200]
    russell=[6,18,18,28,40,50,65,65,72,82,90,99,99,109,109,115,132,143,151,156,160,175]
    piastri=[0,0,4,4,4,5,5,5,5,17,27,34,36,36,42,57,83,83,87,87,89,97]
    stroll=[8,8,20,27,27,27,35,37,44,44,45,47,47,47,47,47,47,53,53,63,73,74]
    gasly=[2,4,4,4,8,14,15,15,16,16,16,22,37,37,45,46,46,56,56,62,62,62]
    ocon=[0,4,4,4,6,21,25,29,31,31,31,35,36,36,36,38,44,44,45,46,58,58]
    albon=[1,1,1,1,1,1,1,7,7,11,11,11,15,21,21,21,23,25,27,27,27,27]
    yuki=[0,0,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,8,8,13,13,17]
    bottas=[4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,10,10,10,10,10,10]
    hulkenberge=[0,0,6,6,6,6,6,6,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    ricciardo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6]
    zhou=[0,0,2,2,2,2,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6]
    magnussen=[0,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
    sargeant=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
    st.subheader('Driver Points 2023 Race by Race')
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=race_loc,y=max_v,mode='markers+lines',name='Max'))
    fig.add_trace(go.Scatter(x=race_loc,y=perez,mode='markers+lines',name='Perez'))
    fig.add_trace(go.Scatter(x=race_loc,y=lewis,mode='markers+lines',name='Lewis'))
    fig.add_trace(go.Scatter(x=race_loc,y=alonso,mode='markers+lines',name='Alonso'))
    fig.add_trace(go.Scatter(x=race_loc,y=charles,mode='markers+lines',name='Charles'))
    fig.add_trace(go.Scatter(x=race_loc,y=norris,mode='markers+lines',name='Norris'))
    fig.add_trace(go.Scatter(x=race_loc,y=sainz,mode='markers+lines',name='Sainz'))
    fig.add_trace(go.Scatter(x=race_loc,y=russell,mode='markers+lines',name='Russell'))
    fig.add_trace(go.Scatter(x=race_loc,y=piastri,mode='markers+lines',name='Piastri'))
    fig.add_trace(go.Scatter(x=race_loc,y=stroll,mode='markers+lines',name='Stroll'))
    fig.add_trace(go.Scatter(x=race_loc,y=gasly,mode='markers+lines',name='Gasly'))
    fig.add_trace(go.Scatter(x=race_loc,y=ocon,mode='markers+lines',name='Ocon'))
    fig.add_trace(go.Scatter(x=race_loc,y=albon,mode='markers+lines',name='Albon'))
    fig.add_trace(go.Scatter(x=race_loc,y=yuki,mode='markers+lines',name='Yuki'))
    fig.add_trace(go.Scatter(x=race_loc,y=bottas,mode='markers+lines',name='Bottas'))
    fig.add_trace(go.Scatter(x=race_loc,y=hulkenberge,mode='markers+lines',name='Hulkenberg'))
    fig.add_trace(go.Scatter(x=race_loc,y=ricciardo,mode='markers+lines',name='Ricciardo'))
    fig.add_trace(go.Scatter(x=race_loc,y=zhou,mode='markers+lines',name='Zhou'))
    fig.add_trace(go.Scatter(x=race_loc,y=magnussen,mode='markers+lines',name='Magnussen'))
    fig.add_trace(go.Scatter(x=race_loc,y=sargeant,mode='markers+lines',name='Sargeant'))


    fig.update_layout(
            xaxis=dict(title='Race', tickangle=90),
            yaxis=dict(title='Driver Points'),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=40, r=40, t=80, b=40),
            hovermode='closest',
            plot_bgcolor='white',
            paper_bgcolor='rgb(80, 82, 87)'
        )

    # Display the plot
    st.plotly_chart(fig)

    st.subheader('Constructor Points 2023 Race by Race')
    race_loc=['Bahrain','Saudi Arabia','Australia','Azerbaijan','Miami', 'Monaco','Spanish','Canadian','Austria', 'British','Hungarian','Belgian','Dutch','Italian','Singapore','Japanese','Qatar','United States','Mexican','Brazilian','Las Vegas','Abu Dhabi']
    redbull=[x+y for x,y in zip(max_v,perez)]
    mercedes=[x+y for x,y in zip(lewis,russell)]
    ferrari=[x+y for x,y in zip(charles,sainz)]
    mclaren=[x+y for x,y in zip(norris,piastri)]
    aston_martin=[x+y for x,y in zip(alonso,stroll)]
    alpine=[x+y for x,y in zip(gasly,ocon)]
    alphatauri=[x+y for x,y in zip(yuki,ricciardo)]
    williams=[x+y for x,y in zip(albon,sargeant)]
    haas=[x+y for x,y in zip(hulkenberge,magnussen)]
    alpharomeo=[x+y for x,y in zip(bottas,zhou)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=race_loc,y=redbull,mode='markers+lines',name='redbull'))
    fig.add_trace(go.Scatter(x=race_loc,y=mercedes,mode='markers+lines',name='mercedes'))
    fig.add_trace(go.Scatter(x=race_loc,y=ferrari,mode='markers+lines',name='ferrari'))
    fig.add_trace(go.Scatter(x=race_loc,y=mclaren,mode='markers+lines',name='mclaren'))
    fig.add_trace(go.Scatter(x=race_loc,y=aston_martin,mode='markers+lines',name='aston martin'))
    fig.add_trace(go.Scatter(x=race_loc,y=alpine,mode='markers+lines',name='alpine'))
    fig.add_trace(go.Scatter(x=race_loc,y=williams,mode='markers+lines',name='williams'))
    fig.add_trace(go.Scatter(x=race_loc,y=alphatauri,mode='markers+lines',name='alphatauri'))
    fig.add_trace(go.Scatter(x=race_loc,y=alpharomeo,mode='markers+lines',name='alpharomeo'))
    fig.add_trace(go.Scatter(x=race_loc,y=haas,mode='markers+lines',name='haas'))
    

    fig.update_layout(
            xaxis=dict(title='Race', tickangle=90),
            yaxis=dict(title='Constructor Points'),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=40, r=40, t=80, b=40),
            hovermode='closest',
            plot_bgcolor='white',
            paper_bgcolor='rgb(80, 82, 87)'
        )
    
    # Display the plot
    st.plotly_chart(fig)

    st.subheader('Lewis Hamilton vs Max Verstappen')

    year=[2015,2016,2017,2018,2019,2020,2021,2022,2023]
    max_verstappen=[49,204,168,249,278,214,395.5,454,575]
    lewis_hamilton=[381,380,363,408,413,347,387.5,240,234]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=year,y=max_verstappen,mode='markers+lines',name='Max Verstappen'))
    fig.add_trace(go.Scatter(x=year,y=lewis_hamilton,mode='markers+lines',name='Lewis Hamilton'))

    fig.update_layout(
            xaxis=dict(title='Year', tickangle=90),
            yaxis=dict(title='Points'),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=40, r=40, t=80, b=40),
            hovermode='closest',
            plot_bgcolor='white',
            paper_bgcolor='rgb(80, 82, 87)'
        )
    
    # Display the plot
    st.plotly_chart(fig)
    st.subheader('Redbull vs Mercedes vs Ferrari')

    years=[2018,2019,2020,2021,2022,2023]
    redbull1=[419,417,319,585.5,759,860]
    mercedes1=[655,739,573,613.5,515,409]
    ferrari1=[571,504,131,323.5,554,406]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years,y=redbull1,mode='markers+lines',name='RedBull'))
    fig.add_trace(go.Scatter(x=years,y=mercedes1,mode='markers+lines',name='Mercedes'))
    fig.add_trace(go.Scatter(x=years,y=ferrari1,mode='markers+lines',name='Ferrari'))


    fig.update_layout(
            xaxis=dict(title='Year', tickangle=90),
            yaxis=dict(title='Points'),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=40, r=40, t=80, b=40),
            hovermode='closest',
            plot_bgcolor='white',
            paper_bgcolor='rgb(80, 82, 87)'
        )
    
    # Display the plot
    st.plotly_chart(fig)
