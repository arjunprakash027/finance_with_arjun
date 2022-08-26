import streamlit as st
from explore import finance_explore
from footsy import footer
from news import stock_news

page = st.sidebar.radio("Select a page",
("news",
"explore"))


footer()

if page == "news":
    stock_news()
    footer()

if page == "explore":
    finance_explore()
    footer()