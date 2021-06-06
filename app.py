import streamlit as st
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
