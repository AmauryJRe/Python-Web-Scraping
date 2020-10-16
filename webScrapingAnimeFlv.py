import requests
import lxml.html
import os
import json

SITE_URL='https://www3.animeflv.net/'

father = requests.get("https://www3.animeflv.net/browse?status%5B%5D=1&order=default")
docFather = lxml.html.fromstring(father.content)
paginator=docFather.xpath('//ul[@class="pagination"]')[0]
urls=paginator.xpath('.//a/@href')[1:-1]
list = {}

for url in urls:
    html =  requests.get(f"{SITE_URL}{url}")
    doc = lxml.html.fromstring(html.content)
    articles = doc.xpath('//article[@class="Anime alt B"]')
    for article in articles:
        number = str(article.xpath('.//img/@src'))[-10:-6]
        name = str(article.xpath('.//h3[@class="Title"]/text()')[0])
        list[number]=name.replace(':','-')
        list[number]=name.replace('\t','')

with open('/media/amaury/DATOS/ANIMES/Utiles/animeList.json', 'w') as file:
    file.write(json.dumps(list))
print('Done')