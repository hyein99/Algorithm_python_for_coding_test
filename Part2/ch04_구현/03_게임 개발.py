# 입력
N, M = map(int, input().split())
x, y, d = map(int, input().split())  # (A, B), 방향

amap = []  # 0(육지), 1(바다)
for _ in range(N):
    amap.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]
cnt, result = 0, 1  # 방향 회전 수, 방문한 칸의 수
amap[x][y] = 1
while True:
    # 4방향 모두 탐색한 경우
    if cnt == 4:
        nx, ny = x+dx[(d+2)%4], y+dy[(d+2)%4]
        if nx<0 or nx>N-1 or ny<0 or ny>M-1 or amap[nx][ny] != 0:
            break
        else:
            x, y = nx, ny
            amap[x][y] = 1
            result += 1
            cnt = 0
            continue

    # 왼쪽으로 회전
    d = (d+3)%4
    nx, ny = x+dx[d], y+dy[d]
    if 0<=nx<N and 0<=ny<M and amap[nx][ny] == 0:
        x, y = nx, ny
        amap[x][y] = 1
        result += 1
        cnt = 0
    else:
        cnt += 1

print(result)