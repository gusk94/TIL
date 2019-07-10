# 강사님 내용
import requests
import bs4
import csv

# 1. Bithumb 페이지를 가지고 온다.
responce = requests.get('https://www.bithumb.com/')
html = responce.text # 응답받은 객체에서 html 문서를 string으로 가지고 옴 <= html의 타입 : 'str'

# 2. Beautiful Soup 모듈을 이용하여 string type의 html을 파싱한다!
soup = bs4.BeautifulSoup(html, 'html.parser') # html.text를 객체로 만들어 가지고 올 수 있게 만듦

# 3. 각 코인의 정보가 담겨있는 table row 데이터를 list의 형태로 가져온다.
coins = soup.select('.coin_list tr') # 하위 데이터 호출 -> 띄어쓰기 : 직속 데이터 + ...로 아래 있는 모든 tr을 가져옴 / > : 직속 데이터만 가져옴

# 5. csv writer 를 이용해서 정보를 저장한다.
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

    # 4. 각 코인을 순회하며 필요한 정보만 추출한다.
    for coin in coins: # 각 코인의 이름과 시세 데이터를 추출
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW','').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        csv_writer.writerow(data)
