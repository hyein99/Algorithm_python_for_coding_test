# https://www.acmicpc.net/problem/18405

from collections import defaultdict

def spreadVirus():
    for i in range(1, K+1):
        # i번째 바이러스 증식(번호가 낮은 종류의 바이러스부터 증식)
        nextVirus = []
        for (x, y) in virus[i]:
            for d in dir:
                nx, ny = x+d[0], y+d[1]
                if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                    graph[nx][ny] = i
                    nextVirus.append((nx, ny))
        virus[i] = nextVirus


# 입력
N, K = map(int, input().split())  # N*N 시험관, K: 바이러스 종류
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())
dir = [(1,0), (-1,0), (0,1), (0,-1)]

# 바이러스 종류에 따른 위치 표시
virus = defaultdict(list)
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i, j))

# S초가 지난 후에 (X, Y)에 존재하는 바이러스 종류 출력
for _ in range(S):
    spreadVirus()
print(graph[X-1][Y-1])