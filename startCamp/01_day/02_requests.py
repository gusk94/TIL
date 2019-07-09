import requests #pip install ()
import bs4 #Beautiful Soup

url = 'https://finance.naver.com/sise/'

response = requests.get(url) #response.text -> 문자열 반환
html = response.text

soup = bs4.BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text #KOSPI_now : 아이디를 바로 불러옴
print(kospi)
