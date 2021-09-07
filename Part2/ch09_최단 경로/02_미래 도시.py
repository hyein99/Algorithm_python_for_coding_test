# 1~N: 도로를 통해 연결
# 1번 회사에서 X번 회사에 방문해 물건 판매
# 양방향 이동, 1시간으로 이동 가능
# 1 > K > X

def floyd():
    for i in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

INF = int(1e9)

# 입력
N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
X, K = map(int, input().split())

# 자기자신에서 자기자신으로 가는 경우
for i in range(N):
    graph[i][i] = 0

floyd()
result = graph[0][K-1] + graph[K-1][X-1]
if result >= INF:
    print(-1)
else:
    print(result)