import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Raf's Website", page_icon="📊")
# Hide footer and menu, No need in my website
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>""", unsafe_allow_html=True)

'''
# Hello, welcome to my website
My name is Rafael Mello, I work as a Data Engineer in Melbourne, Australia

I made this website mostly mostly for fun and a little for profit
## About Me
**Headline is:** I am passionate and excited data engineer and I love nerding out on data products.
I like to think about how companies use their data in creative ways but I also like thinking about security, privacy and fair ml.

I have lived and worked in a few different places:
'''
st.sidebar.title("Contents")


df = pd.DataFrame({
    'awesome cities' : ['Melbourne / Australia', 'Florianópolis / Brazil', 'Campinas / Brazil', 'Ottawa / Canada'],
    'lat' : [-37.8136, -27.5986,  -22.91008, 45.4177916],
    'lon' : [144.9631, -48.497775, -47.067559,  -75.66981757]
})

st.pydeck_chart(
    pdk.Deck(
        map_style='mapbox://styles/rafaelathaydemello/ckpl4nrw30rna17odfdcoud6v',
        initial_view_state=pdk.ViewState(
                latitude=-13.257081386404316,
                longitude=16.574100325225142,
                zoom=0.5,
                # pitch=60
            ),
        layers=[pdk.Layer(
            'ScatterplotLayer',
            data=df,
            filled=True,
            # pickable=True,
            get_position='[lon, lat]',
            get_fill_color=[0, 0, 255],
            radius_min_pixels=6,
            radius_max_pixels=7,
        )],
        # tooltip={'hey' : "come here"}
        ))
