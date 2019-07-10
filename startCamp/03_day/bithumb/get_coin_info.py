import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bithumb.com/'

selector1 = '#tableAsset > tbody > tr > td > p > a > strong'
selector2 = '.sort_real'

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
coins1 = soup.select(selector1)
coins2 = soup.select(selector2)

keys, values = [], []

for coin1 in coins1:
    keys += [coin1.text]

for coin2 in coins2:
    values += [coin2.text]

coin = dict(zip(keys,values))

with open('bitumb.csv', 'w', encoding='utf-8', newline="") as f:
    bit = csv.writer(f)
    for item in coin.items():
        bit.writerow(item)
        