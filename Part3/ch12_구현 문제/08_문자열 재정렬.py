# 알파벳 대문자와 숫자로만 구성된 문자열
# 알파벳 오름차순으로 정렬하고 뒤에 숫자를 다 더해서 출력

S = input()
arr = []
num = 0
for s in S:
    if s.isdigit():
        num += int(s)
    else:
        arr.append(s)
arr.sort()
arr.append(num)

print(*arr, sep='')