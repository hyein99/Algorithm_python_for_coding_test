# https://www.acmicpc.net/problem/18352
# N개의 도시, M개의 도로
# 모든 도로의 거리 1
# 특정 도시 X르 부터 출발하여 도달할 수 있는 모든 도시 중에 최단 거리가 K인 도시 번호 출력

import sys
from collections import defaultdict
from collections import deque

def BFS(X):
    qu = deque()
    qu.append(X)
    dist[X] = 0

    while qu:
        node = qu.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node]+1
                qu.append(next_node)

# 입력
N, M, K, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

# X로 부터 최단 거리 계산
dist = [-1 for _ in range(N + 1)]  # dist[i]: i까지의 최단거리
BFS(X)

# 출력
exist = False
for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        exist = True

if not exist:
    print(-1)