from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from sklearn.model_selection import train_test_split
# html = "https://southpark.fandom.com/wiki/List_of_Episodes#"
# html_page = requests.get(html, headers={'User-Agent': 'Mozilla/5.0'})
# soup = BeautifulSoup(html_page.content, 'html.parser')


# def grab_urls(soup):
#     episode_urls = []
#     for season in soup.findAll('td', style="font-size:125%"):
#         for episode in season.findAll('a'):
#             try:
#                 episode_urls.append(episode.attrs['href'])
#             except:
#                 continue

#     return episode_urls

# urls = grab_urls(soup)

# ========================= Uncomment after test is done =======================

# for i in urls:
#     if i != "/wiki/TBA":
#         html = "https://southpark.fandom.com" + i + "/Script"
#         html_page = requests.get(
#             html, headers={'User-Agent': 'Mozilla/5.0'})
#         soup = BeautifulSoup(html_page.content, 'html.parser')
#         # print(soup)
#
#         with open("episode_urls.txt", "a") as file:
#             file.write(html + "\n")
#
characters = []
lines = []
# ---------------------------Uncomment after test ---------------------

# for x in soup.findAll('td', {"class": "DLborderBOT DLborderRIGHT"}):
#     if x.text.replace('\n', '') != "":
#         characters.append(x.text.replace('\n', ''))
#         lines.append(x.nextSibling.text.replace('\n', ''))
#         print(characters)
#     else:
#         continue
test_url = "https://southpark.fandom.com/wiki/Credigree_Weed_St._Patrick%27s_Day_Special/Script"

with open("episode_urls.txt", "r") as list_of_episodes:
    episodes = list_of_episodes.readlines()
    for url in episodes:
        html_contents = requests.get(url.strip(), headers={'User-Agent': 'Mozilla/5.0'})
        episode_soup=BeautifulSoup(html_contents.content, "html.parser")
        script=episode_soup.findAll('tr', {"class": "", "style": ""})
        for rows in script:
            character_row=rows.find_all("td", {"class": "DLborderBOT DLborderRIGHT"})
            for character in character_row:
                if character.text == '':
                    character.text='setting'
                characters.append(character.text.strip())
            line_row=rows.find_all("td", {"style": "padding-left:5px;"})
        # characters.append(character_row)
            for line in line_row:
                lines.append(line.text.strip())

# html_contents = requests.get(test_url, headers={'User-Agent': 'Mozilla/5.0'})
# episode_soup = BeautifulSoup(html_contents.content, "html.parser")
# print(episode_soup)

print(len(lines))
print(len(characters))

'''
----------------------------------------------------------------
Check if there are empty strings
----------------------------------------------------------------
'''

def is_empty_or_blank(msg):
    """ This function checks if given string is empty
     or contain only shite spaces"""
    return re.search("^\s*$", msg)


for char in characters:
    if len(char) == 0:
        char.replace("", "setting")

result=any([is_empty_or_blank(elem) for elem in characters])
if result:
    # print('Yes, list contains one or more empty strings')
    [ch.replace(str(result), 'setting') for ch in characters]
else:
    print('List does not contains any empty string')

print(characters[0])
# print(lines)
df=pd.DataFrame({'Character': characters, 'line': lines})
print(df)
# with open('script.txt', 'w') as script_file:
#     script_file.write(str(df))
# print(df.head())