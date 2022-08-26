import streamlit as st
import requests
from bs4 import BeautifulSoup



def stock_news():
    headlines = []
    linkz = []
    imgz = []
    resp = requests.get("https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms")
    soup = BeautifulSoup(resp.content, features='xml')
    k = soup.findAll('title')
    lnk =soup.findAll('link')
    img = soup.findAll('image')

    for txt in k:
        #print(txt.get_text())
        headlines.append(txt.get_text())

    for links in lnk:
        #print(links.get_text())
        linkz.append(links.get_text())

    for im in img:
        #print(im.get_text())
        imgz.append(links.get_text())


    linkz = linkz[2:len(linkz)]
    headlines = headlines[2:len(headlines)]

    st.title('Top Stock headlines for today')

    for i in range(2,len(headlines)):

        with st.expander(headlines[i]):
            st.write(linkz[i])