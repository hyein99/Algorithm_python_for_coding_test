# https://www.acmicpc.net/problem/14502

import copy

maxSafeZone = 0

def putWall(cnt, startx, starty):
    # startx, starty: 이미 탐색한 구역에 벽을 세우지 않도록 확인 완료한 구간 표시
    global maxSafeZone

    if cnt == 0:
        # step 2) 벽 3개 세우면 바이러스 퍼뜨리기
        safeZone = spreadVirus(graph)
        # step 4) 안전영역 최대 크기 구하기
        maxSafeZone = max(maxSafeZone, safeZone)

        return

    # step 1) 벽 세우기 (벽 3개 무조건 세워야함)
    for i in range(startx, N):
        for j in range(M):
            if i <= startx and j < starty:
                continue
            if graph[i][j] == 0:
                graph[i][j] = 1
                putWall(cnt - 1, i, j+1)
                graph[i][j] = 0


def spreadVirus(graph):
    # 초기 바이러스 위치 append
    qu = []
    for (i, j) in virus:
        qu.append((i, j))

    tmp = copy.deepcopy(graph)

    while qu:
        x, y = qu.pop()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                qu.append((nx, ny))

    # step 3) 안전영역 크기 구하기
    cnt = countSafeZone(tmp)
    # print(*tmp, sep='\n')
    # print(cnt)
    return cnt


def countSafeZone(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


# 입력
N, M = map(int, input().split())  # 연구소 크기: N*M
graph = []                        # 0: 빈칸, 1: 벽, 2: 바이러스
for _ in range(N):
    graph.append(list(map(int, input().split())))

dir = [(1,0), (0,1), (-1,0), (0,-1)]
virus = []          # 초기 바이러스 리스트
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))

# 안전영역의 크기 최대값 출력
putWall(3, 0, 0)
print(maxSafeZone)