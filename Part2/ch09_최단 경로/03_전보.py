# N개도시
# X > Y 전보: 통로가 있어야 보냄
# C에서 최대한 많은 도시로 메시지 보내야 함
# 도시 개수, 시간 출력

import heapq
from collections import defaultdict

INF = int(1e9)
def dijkstra(start):
    Q = []
    heapq.heappush(Q, [0, start])
    dist[start] = 0

    while Q:
        time, node = heapq.heappop(Q)

        # 현재 노드가 이미 처리된 적이 있으면 무시
        if dist[node] < time:
            continue

        for y, z in graph[node]:
            if dist[y] > time + z:
                heapq.heappush(Q, [time+z, y])
                dist[y] = time+z


# 입력
N, M, C = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z]) # X에서 Y까지 비용 Z

dist = [INF] * (N+1)
dijkstra(C)

# 출력
cnt = 0
max_distance = 0
for d in dist:
    if d < INF:
        cnt += 1
        max_distance = max(max_distance, d)

# 시작노드는 제외
print(cnt-1, max_distance)