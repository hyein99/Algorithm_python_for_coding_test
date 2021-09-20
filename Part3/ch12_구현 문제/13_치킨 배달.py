# https://www.acmicpc.net/problem/15686

from collections import defaultdict

# 입력
N, M = map(int, input().split())  # N: 도시크기, M: 최대 치킨집 개수
board = []
chicken = []           # 치킨 집 리스트
chicken_dist = dict()  # 각 집의 치킨거리
for i in range(N):
    arr = list(map(int, input().split()))  # 1: 집, 2: 치킨집
    board.append(arr)
    for j in range(len(arr)):
        if arr[j] == 2:
            chicken.append((i, j))
        elif arr[j] == 1:
            chicken_dist[(i, j)] = 0

# step 1) 치킨 집 M개 선택하는 경우의 수
select_chicken = []

# step 2) 해당 치킨집을 기준으로 각 집이 치킨거리 구하기

# step 3) 도시의 치킨거리 구하기(최소값)
