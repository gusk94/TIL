from flask import Flask, render_template, request # 사용자의 요청을 확인할 수 있음, requests와 다르다
import requests
app = Flask(__name__)


@app.route('/') # / => root
def index():
    return 'Hello World'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', name = name)


@app.route('/ping')
def ping():
    return render_template('ping.html' )


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return  render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # Message
    # Ascii Art API 를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}').text
    result = response
    return render_template('ascii_result.html', result=result)


# 사용자가 정보를 입력하는 페이지 / 정보를 제출한 후 처리하는 페이지 필요
@app.route('/lotto_input')
def lotto_input():
    # 사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    # 사용자 입력 값 받기
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split()
    infos = []
    re = 0

    # 로또 실제 당첨번호 확인
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # json 타입의 파일을 python dictionary로 parsing

    for i in range(1, 7):
        infos.append(str(lotto_info[f'drwtNo{i}']))

    # 번호 교집합 개수 찾기
    if len(lotto_numbers) == 6:
        matched = 0
        for number in lotto_numbers:
            if number in infos:
                matched += 1

        if matched == 6:
            result = '1st'
        elif matched == 5:
            if str(lotto_info['bnusNo']) in lotto_numbers:
                result = '2nd'
            else:
                result = '3rd'
        elif matched == 4:
            result = '4rd'
        elif matched == 3:
            result = '5rd'
        else:
            result = '꽝입니다'
    else:
        result = '다시 입력해주세요'


    # for info in infos:
    #     for lotto_number in lotto_numbers:
    #         if info == lotto_number:
    #             re += 1


    return render_template('lotto_result.html',lotto_round=lotto_round, lotto_number=lotto_numbers, info=infos, result=result)


if __name__ == '__main__': 
    app.run(debug=True)
    