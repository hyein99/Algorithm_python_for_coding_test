# 위상 정렬 알고리즘 응용
## 각 노드에 대해 인접한 노드를 확인할 때, 인접한 노드에 대해 현재보다 강의시간이 더 긴 경우를 찾는다면,
## 더 오랜 시간이 걸리는 경우의 시간 값을 저장하여 결과 테이블 갱신

from collections import deque

def topolgy_sort():
    qu = deque()

    for i in range(N):
        if indegree[i] == 0:
            qu.append(i)

    while qu:
        now = qu.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                qu.append(i)


# 입력
N = int(input())                # 동빈이가 듣고자 하는 강의의 수
indegree = [0] * N              # 모든 노드에 대한 진입차수 0으로 초기화
graph = [[] for i in range(N)]  # 각 노드에 연결된 간선정보 graph[i]: i가 선수과목인 과목들
time = [0] * N                  # 각 강의 시간
result = [0] * N                # 결과값
for i in range(N):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    result[i] = arr[0]
    for x in arr[1:-1]:
        indegree[i] += 1
        graph[x-1].append(i)

topolgy_sort()
for i in range(N):
    print(result[i])