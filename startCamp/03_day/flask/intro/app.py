from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route("/") # 데코레이터 / endpoint를 정의 / 특정 endpoint로 왔을 때 아래 함수를 실행시켜 사용자가 브라우저에서 볼 화면 지정
def hello(): # 함수 만드는 방법
    return "Hello k!"

@app.route('/ssafy')
def ssafy(): # 함수 이름 -> 다른 함수와 겹치지 x
    return 'Hello SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019,9,3)
    td = b_day - today
    return f'{td.days} 일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''
# Variable Routing
@app.route('/greeting/<name>')
def greeting(name): # name == IU
    return f'반갑습니다! {name} 님!'

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 3 제곱은 {number ** 3} 입니다.'

# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥', '라면', '냉모밀']
    order = random.sample(menu, people)
    return str(order)

if __name__ == '__main__': 
    app.run(debug=True)