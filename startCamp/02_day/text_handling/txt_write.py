# 열기모드
# r : 읽기, w : 쓰기(write - 오버라이트(덮어쓰기)), a : 추가(append)
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'this is line {i+1} \n')
f.close()

# with : 컨텍스트 매니저, 작업하는 코드블록 생성(안쪽에서 작업할 수 있게) -> close 사용하지 않아도 닫아줌

with open('with_ssafy.txt', 'w') as f: # 생성한 파일의 이름을 f로 준다
    for i in range(10):
        f.write(f'this is line {i+1} \n')

with open('ssafy.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])

