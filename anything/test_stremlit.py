import streamlit as st
import requests
from bs4 import BeautifulSoup
r = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
with open('proxy.txt', 'a') as f1:
            print(r, file=f1)
with open("proxy.txt", "r") as file1:
    for line in file1:
        if line.find(':') > -1:
            print(line.strip().split(':')[0])
#st.write(r)