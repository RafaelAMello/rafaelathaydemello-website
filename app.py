import streamlit as st
# from src import WELCOME_PAGE

# Hide footer and menu, No need in my website
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>""", unsafe_allow_html=True)
'''
# Hello, welcome to my website
My name is Rafael Mello, I work as a Data Engineer in Melbourne, Australia

I made this website mostly mostly for fun and a little for profit
'''
st.sidebar.title("Contents")
