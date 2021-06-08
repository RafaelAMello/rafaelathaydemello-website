from datetime import datetime

import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt

def load_data() -> pd.DataFrame:
    return pd.read_json('data/places.json')

def get_lived_data(df: pd.DataFrame) -> pd.DataFrame:
    df_lived = df[pd.notna(df['start_year'])]
    df_lived['start_datetime'] = df_lived['start_year'].apply(lambda x : datetime(year=int(x), month=1, day=1))
    df_lived['end_datetime'] = df_lived['end_year'].apply(lambda x : datetime(year=int(x), month=1, day=1)if pd.notna(x) else x)
    df_lived['end_datetime'] = df_lived['end_datetime'].fillna(datetime.now())
    df_lived['days'] = (df_lived['end_datetime'] - df_lived['start_datetime']).dt.days
    return df_lived

def about_me():
    st.markdown('''
    # About Me
    I am passionate and excited data engineer and I love nerding out on data products (kinda like this one).
    I like to think about how companies use their data in creative ways but I also like thinking about security, privacy and fair ml.

    I have lived and worked in a few different places.
    ## Here they are in map form:
    ''')

    df = load_data()
    col1, col2 = st.beta_columns(2)
    western = col2.button("Focus on Eastern Hemisphere")
    eastern = col1.button("Focus on Western Hemisphere")
    western_start_point = dict(
        latitude=-37.8136,
        longitude=144.9631,
        zoom=12,
    )
    eastern_start_point = dict(
        latitude=18.80105460090463,
        longitude=-72.31192900368677,
        zoom=1.5
    )
    if western:
        start_point = western_start_point
    elif eastern:
        start_point = eastern_start_point
    else:
        start_point = western_start_point
    st.pydeck_chart(
        pdk.Deck(
            map_style='mapbox://styles/rafaelathaydemello/ckpl4nrw30rna17odfdcoud6v',
            initial_view_state=pdk.ViewState(**start_point),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df[['location', 'country', 'dot_color', 'lat', 'lon', 'desc']],
                    filled=True,
                    pickable=True,
                    get_position='[lon, lat]',
                    get_fill_color='dot_color',
                    radius_min_pixels=6,
                    radius_max_pixels=7,
                )
            ],
            tooltip={'text' : "{location} / {country} \n{desc}"}
            ), use_container_width=True)

    st.markdown('''
    ## Here they are in bar chart form:
    ''')
    df_lived = get_lived_data(df)
    df_lived[['days']]

    chart = alt.Chart(df_lived[['location', 'days', 'country', 'desc']].sort_values('days')).mark_bar().encode(
        x='days',
        y='location',
        color='country',
        tooltip=['desc']
    ).interactive()
    chart.height = 400
    st.altair_chart(chart, use_container_width=True)
