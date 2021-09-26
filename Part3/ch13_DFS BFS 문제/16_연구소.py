# https://www.acmicpc.net/problem/14502

from collections import deque

def putWall(cnt, maxSafeZone, startx, starty):
    if cnt == 0:
        # step 2) 벽 3개 세우면 바이러스 퍼뜨리기
        safeZone = spreadVirus(graph)

        # step 4) 안전영역 최대 크기 구하기
        maxSafeZone = max(maxSafeZone, safeZone)

        return maxSafeZone

    # step 1) 벽 세우기 (벽 3개 무조건 세워야함)
    for i in range(startx, N):
        for j in range(starty, M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                maxSafeZone = max(maxSafeZone, putWall(cnt-1, maxSafeZone, i, j))
                graph[i][j] = 0

    return maxSafeZone


def spreadVirus(graph):
    # 초기 바이러스 위치 append
    qu = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                qu.append((i, j))

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                qu.append((nx, ny))

    print(*graph, sep='\n')

    # step 3) 안전영역 크기 구하기
    cnt = countSafeZone(graph)
    return cnt


def countSafeZone(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


# 입력
N, M = map(int, input().split())   # 연구소 크기: N*M
graph = []                         # 0: 빈칸, 1: 벽, 2: 바이러스
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 안전영역의 크기 최대값 출력
dir = [(1,0), (0,1), (-1,0), (0,-1)]
maxSafeZone = putWall(3, 0, 0, 0)
print(maxSafeZone)