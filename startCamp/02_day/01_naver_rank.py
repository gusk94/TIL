import requests
from bs4 import BeautifulSoup

url = 'http://www.naver.com'
selector = '.ah_k'

responce = requests.get(url)
html = responce.text

soup = BeautifulSoup(html, 'html.parser')
ranks = soup.select(selector) #요소 검사 내부에서 검색어가 나올때까지의 경로

for rank in ranks:
    print(rank.text)
