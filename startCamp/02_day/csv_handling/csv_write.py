dinner = {
    '양자강' : "02-557-4211", #차돌짬뽕
    '김밥카페' : '02-553-3181', #라돈
    '순남시래기' : '02-508-0887', #보쌈정식
}

# print(dinner.keys()) -> key만 list로 나옴 / dinner.valus() : 값만 리스트형태로 출력 / dinner.items() -> key + value

# 1. String formatting
with open('dinner.csv', 'w', encoding="utf-8") as f:
    for item in dinner.items(): # [['양자강', '02-557-4221], ['김밥카페', '02-553-3181], ['순남시래기', '02-508-0887']] -> 리스트로 변환
        f.write(f'{item[0]},{item[1]}\n') # 양자강,02-557-4221

# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding="utf-8", newline='') as f: # newline을 통해서 각 줄이 띄어지지 않고 붙어서 작성됨 -> option으로 줄때는 newline 안에 ''로 붙어서 작성해야함.
    csv_writer = csv.writer(f) # f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
        