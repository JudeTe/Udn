# coding=UTF-8
#udn新聞第一頁
import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://udn.com/news/breaknews/1/99#breaknews"
response = requests.get(url)
html = BeautifulSoup(response.text)

with open("udntext","w",encoding="utf-8") as files:
    for a in html.find("div",id="breaknews_body").find_all("dt"):
        newsurl = a.find("a")
        try:
            Nresponse = urlopen("https://udn.com"+newsurl["href"])
            Nhtml = BeautifulSoup(Nresponse)
            for content in Nhtml.find("div", id="story_body_content").find_all("p"):
                files.write(content.text)
        except TypeError:
            pass
        continue

with open("udntitle","w",encoding="utf-8") as file:
    for a in html.find("div",id="breaknews_body").find_all("dt"):
        category = a.find("a",class_="cate")
        title = a.find("h2")
        times = a.find("div",class_="dt")
        view = a.find("div",class_="view")
        newsurl = a.find("a")
        try:
            titles = (category.text, times.text, title.text, view.text, "https://udn.com" + newsurl["href"])
            df = pd.DataFrame(columns=[category.text, times.text, title.text, view.text,"https://udn.com" + newsurl["href"]])
            file.write(str(df))
        except AttributeError:
            continue