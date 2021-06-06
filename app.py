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

## About the tech stack
Here is what I used:
- 🖥️ Webapp with python & [Streamlit](https://streamlit.io/)
- 🔨 Packaged with [Docker](https://www.docker.com/)
- 👷 CD with [Github Actions](https://github.com/features/actions)
- ☁️ Running on [AWS Fargate](https://aws.amazon.com/fargate/)
- 🚢 Deployed with [cdk](https://docs.aws.amazon.com/cdk/latest/guide/home.html) on typescript
- 🧑‍💻 Feel free to steal this code on [Github](https://github.com/RafaelAMello/rafaelathaydemello-website)


## About Me
**Headline is:** I am passionate and excited data engineer and I love nerding out on data products.
I like to think about how companies use their data in creative ways but I also like thinking about security, privacy and fair ml.

I have lived and worked in a few different places:
'''
st.sidebar.title("Contents")


df = pd.DataFrame({
    'location' : ['Melbourne / Australia', 'Florianópolis / Brazil', 'Campinas / Brazil', 'Ottawa / Canada', 'HotDoc'],
    'blue' : [255, 255, 255, 255, 0],
    'lat' : [-37.8136, -27.5986,  -22.91008, 45.4177916, -37.820774929870204],
    'lon' : [144.9631, -48.497775, -47.067559,  -75.66981757, 144.9569359345779]
})

# -37.820774929870204, 144.9569359345779
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
            pickable=True,
            get_position='[lon, lat]',
            get_fill_color="[0, 0, blue]",
            radius_min_pixels=6,
            radius_max_pixels=7,
        )],
        tooltip={'text' : "{location}"}
        ))
