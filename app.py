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
    'awesome cities' : ['Melbourne', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [-37.8136, 44.979840,  38.257972, 39.030575],
    'lon' : [144.9631, -93.272474, -85.765187,  -95.702548]
})

# -36.374472626286966, -144.91669951963823
# 26.57278274606463, 50.85144319085214
# -13.257081386404316, 16.574100325225142
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
