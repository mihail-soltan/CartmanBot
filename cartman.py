from bs4 import BeautifulSoup
import requests
import pandas as pd

html = "https://southpark.fandom.com/wiki/List_of_Episodes#"
html_page = requests.get(html, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(html_page.content, 'html.parser')


def grab_urls(soup):
    episode_urls = []
    for season in soup.findAll('td', style="font-size:125%"):
        for episode in season.findAll('a'):
            try:
                episode_urls.append(episode.attrs['href'])
            except:
                continue

    return episode_urls


urls = grab_urls(soup)

for i in urls:
    if i != "/wiki/TBA":
        html = "https://southpark.fandom.com" + i + "/Script"
        html_page = requests.get(
            html, headers={'User-Agent':    'Mozilla/5.0'})
        soup = BeautifulSoup(html_page.content, 'html.parser')
        # print(html)

characters = []
lines = []

for x in soup.findAll('td', {"class": "DLborderBOT DLborderRIGHT"}): 
    if x.text.replace('\n', '') != "":
         characters.append(x.text.replace('\n', ''))
         lines.append(x.nextSibling.text.replace('\n', ''))
         print(characters)
    else:
         continue