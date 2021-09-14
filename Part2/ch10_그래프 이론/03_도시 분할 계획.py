# N개의 집, M개의 길
# 마을 2개로 분할
# 각 분리된 마을 안에 집들이 서로 연결되도록
# 임의의 두 집 사이에 경로가 항상 존재해야 함
# 분리된 두 마을 사이의 길들은 없앨 수 있음
# 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재해야 하고 길을 더 없앨 수 있음
# 길 유지비의 합을 최소로

def find_parent(a):
    if villages[a] != a:
        villages[a] = find_parent(villages[a])
    return villages[a]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        villages[b] = a
    else:
        villages[a] = b

# 입력
N, M = map(int, input().split())
nodes = []
for _ in range(M):
    A, B, C = map(int, input().split()) # A-B 유지비
    nodes.append((C, A, B))

nodes.sort()
villages = [i for i in range(N)]
result = 0
last = 0  # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선의 비용

for node in nodes:
    cost, a, b = node
    if find_parent(a-1) != find_parent(b-1):
        union_parent(a-1, b-1)
        result += cost
        last = cost

print(result-last)

