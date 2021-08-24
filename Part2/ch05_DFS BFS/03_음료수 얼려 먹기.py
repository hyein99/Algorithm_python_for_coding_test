# 풀이 1: DFS
# def dfs(i, j):
#     done = []
#     st = [(i, j)]
#
#     while st:
#         x, y = st.pop()
#         if (x, y) not in done:
#             done.append((x, y))
#             for d in dir:
#                 nx, ny = x+d[0], y+d[1]
#                 if 0<=nx<N and 0<=ny<M and arr[nx][ny] == '0':
#                     arr[nx][ny] = '1'
#                     st.append((nx, ny))
#
# # 입력
# N, M = map(int, input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(input()))
#
# dir = [(1,0), (-1,0), (0, 1), (0, -1)]
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '0':
#             dfs(i, j)
#             cnt += 1
# print(cnt)

from collections import deque

# 풀이 2: BFS
def bfs(i, j):
    done = [(i, j)]
    qu = deque()
    qu.append((i, j))

    while qu:
        x, y = qu.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if (nx, ny) not in done:
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '0':
                    arr[nx][ny] = '1'
                    qu.append((nx, ny))

# 입력
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

dir = [(1,0), (-1,0), (0, 1), (0, -1)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            bfs(i, j)
            cnt += 1
print(cnt)