import streamlit as st

def homepage():
    st.markdown('''
    # Hello, welcome to my website
    My name is Rafael Mello, I work as a Data Engineer in Melbourne, Australia

    I made this website mostly mostly for fun and a little for profit

    ## What do I have on here?
    Mainly a showcase of expirements and trials, nothing too fancy or pretty, just me messing around. Use the naviagtion bar to select what you want to see
    - **About Me** should tell you a little about yours truly, some mapping, some graphing and some jokes
    - **Finance** is where I talk about finance, I share some highlights of what I have learnt and talk about investing
    - **Deploying Streamlit** is where I talk about how I got this App up and running, I even have some delicious AWS architecture diagrams for the nerds and up to date costs
    - **Data Science Adventures** is me documenting my misguded attempts to do data science, some of it goes well, most of it does not

    ## About the tech stack
    Here is what I used:
    - π₯οΈ Webapp with python & [Streamlit](https://streamlit.io/)
    - πΊοΈ Mapping with [Pydeck](https://deckgl.readthedocs.io/en/latest/) & [Mapbox](https://www.mapbox.com/)
    - π Graphing with [Altair](https://altair-viz.github.io/) and [plotly](https://plotly.com/python/)
    - π¨ Packaged with [Docker](https://www.docker.com/)
    - π· CD with [Github Actions](https://github.com/features/actions)
    - βοΈ Running on [AWS Fargate](https://aws.amazon.com/fargate/)
    - π’ Deployed with [cdk](https://docs.aws.amazon.com/cdk/latest/guide/home.html) on typescript
    - π§βπ» Feel free to steal this code on [Github](https://github.com/RafaelAMello/rafaelathaydemello-website)
''')
