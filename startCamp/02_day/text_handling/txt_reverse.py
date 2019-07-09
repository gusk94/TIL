f = open('ssafy.txt', 'r')
r = open('reversed_ssafy.txt', 'w')

lines = f.readlines()

lines.reverse() # list를 반대로 뒤집는다.
print(lines)

for line in lines:
    r.write(line)

f.close()
r.close()