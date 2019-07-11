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


if __name__ == '__main__': 
    app.run(debug=True)
    