# 왕실의 나이트
# 나이트: L자 형태로 이동(정원 밖으로 이동 x)
# 나이트가 이동할 수 있는 경우의 수 출력

# 입력
ex = input()
x, y = int(ex[1]), ord(ex[0])-ord('a')+1
dx = [-1, 1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

cnt = 0
for i in range(8):
    if 0<x+dx[i]<=8 and 0<y+dy[i]<=8:
       cnt += 1

print(cnt)