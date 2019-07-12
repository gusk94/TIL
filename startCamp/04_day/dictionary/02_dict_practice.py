# """
# Python dictionary 연습 문제
# """

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
ad1 = 0
for value in score.values():
    ad1 += value
result = ad1/len(score)
print(result)





# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sum1, count = 0, 0
for value in scores.values():
    sum1 += sum(value.values())
    count += len(value)
print(sum1/count)
    





# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
a = sum(city['서울'])/len(city['서울'])
b = sum(city['대전'])/len(city['대전'])
c = sum(city['광주'])/len(city['광주'])
d = sum(city['부산'])/len(city['부산'])
print('서울 : ', f'{a:.2f}')
print('대전 : ', b)
print('광주 : ', f'{c:.2f}')
print('부산 : ', d)

# for key, value in city.items():
#     av = sum(value) / len(value)
#     print(f'{key} : {av}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
w = []
for value in city.values():
    for i in range(0, len(value)):
        w.append(value[i])

hot = max(w)
cold = min(w)

for key, value in city.items():
    for i in range(0, len(value)):
        if hot == value[i]:
            print('가장 더운 곳 : ', key)
        elif cold == value[i]:
            print('가장 추운 곳 : ', key)
    
    



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
for i in range(0, len(city['서울'])):
    if city['서울'][i] == 2:
        x = 'O'
    else:
        x = 'X'
print(x)