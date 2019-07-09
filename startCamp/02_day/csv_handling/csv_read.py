# 1. split
with open('dinner.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(',')) # strip() : 개행 문자 제거 / split() : , 기준으로 문자열을 split한다(리스트형태)

# 2. csv reader
import csv
with open('dinner.csv', 'r', encoding='utf-8') as f: #encoding : 한글, 한자, 이모티콘과 같은 것들 -> 몇개가 합쳐진 형태 -> 해석 위해 사용
    items = csv.reader(f)
    for item in items:
        print(item)
