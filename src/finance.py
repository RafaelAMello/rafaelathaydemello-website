import streamlit as st
import pandas as pd
import requests
import plotly.graph_objs as go

def finance():
    st.markdown("""
    # My investment strategy
    By no means I can consider myself a professional investor, but I know a bit. What I do know is that a strategy is important.

    Generally I have been guided by three main principals when I invest:

    ## Thinking 20 years horizon but with a bit of flexibility
    Fortunatly for me I am in good health and in full time work. I have no plans of making any huge life decisions any time soon
    (I have long given up the Australian dream of owning a home, backyards are just not that big a deal for me)
    but I want to be able to make big changes if I want to down the track.

    This puts me in a bit of a tricker situation because I have to pay for that flexibility through having liquid assets but I am willing to pay for that option.

    ## Love me some risk
    Generally I try to get some more aggresive assets - being a 20 something year old means that I know that the rough and the good times
    will smooth out in the long term. And if it doesn't I don't really have that much too loose anyway.

    ## Ethical investments
    As a inner city, latte sipping, good for nothing liberal I generally consider it important that I only invest in things that I consider ethical.
    This looks like me putting [my money in an ethical super fund](https://www.australianethical.com.au/) and prioritising assets who don't have a negative impact on our climate and society.

    ## The breakdown
    With the above in mind I descided to invest mostly in shares with a bit of cash.
    This is what it looks like:
    """)
    df = pd.read_json('data/shares.json')
    pie = go.Figure(
        data=go.Pie(
            labels=df.name,
            values=df.percentage,
        )
    )
    st.plotly_chart(pie)

    st.markdown("""
    ## Individual Assets
    """)
    for n, share_row in df.iterrows():
        if share_row['type'] != 'cash':
            name = share_row['name']
            url = f"https://www.asx.com.au/asx/1/share/{name}"
            payload = requests.get(url)
            data = payload.json()

            st.markdown(f"""**{data['desc_full']}**""")
            if data['open_price'] > data['last_price']:
                color = 'red_down.png'
            else:
                color = 'green_up.png'
            col1, col2, *_ = st.beta_columns(12)
            col1.markdown(f"""${data['last_price']}\n""")
            col2.image(f'data/pics/{color}', width=20)


            st.markdown(f"""
            > Ticker: {data['code']}\n
            > [More info on asx website](https://www2.asx.com.au/markets/company/{data['code']})
            """)
