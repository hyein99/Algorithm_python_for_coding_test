ex = input()
x, y = int(ex[1]), ord(ex[0])-ord('a')+1
dx = [-1, 1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

cnt = 0
for i in range(8):
    if 0<x+dx[i]<=8 and 0<y+dy[i]<=8:
       cnt += 1

print(cnt)