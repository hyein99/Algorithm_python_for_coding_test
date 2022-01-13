# 미로 탈출
# BFS를 이용했을 때 효과적
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문

from collections import deque

def bfs():
    qu = deque()
    qu.append((0, 0))

    while qu:
        x, y = qu.popleft()
        if x==N-1 and y==M-1:
            return dist[x][y]

        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == '1':  # 이동할 수 있는 위치
                maze[nx][ny] = '0'  # 방문표시
                dist[nx][ny] = dist[x][y]+1
                qu.append((nx, ny))


# 입력
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(input()))  # 0: 괴물, 1: 길

dir = [(1,0), (-1,0), (0, 1), (0, -1)]
dist = [[1]*M for _ in range(N)]
print(bfs())
