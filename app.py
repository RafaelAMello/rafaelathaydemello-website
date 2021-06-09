from collections import OrderedDict

import streamlit as st
from email_validator import validate_email, EmailNotValidError
import requests

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

CHOICE = st.sidebar.radio("Go to", options=list(pages.keys()))
pages[CHOICE]()

form = st.sidebar.form(key='contact_form')
form.markdown("## Get in touch (this does nothing)")
email = form.text_input(label='whats your email?')
text = form.text_area(label='Tell me whats on your mind')
contact_submitted = form.form_submit_button('Send off')

if contact_submitted:
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError as e:
        st.sidebar.warning(e)
