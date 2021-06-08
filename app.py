from collections import OrderedDict

import streamlit as st

from src.homepage import homepage
from src.finance import finance
from src.about_me import about_me
from src.tech_stack import tech_stack
from src.data_science import data_science_adventures

st.set_page_config(page_title="Raf's Website", page_icon="📊")
# Hide footer and menu, No need in my website
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
pages = OrderedDict()
pages["Homepage"] = homepage
pages["About Me"] = about_me
pages["Finance stuff"] = finance
pages["The Tech: Deploying Streamlit"] = tech_stack
pages["Data Science Adventures"] = data_science_adventures
# TODO: Contact info

CHOICE = st.sidebar.radio("Go to", options=list(pages.keys()))
pages[CHOICE]()
