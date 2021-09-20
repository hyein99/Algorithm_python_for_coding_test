# https://www.acmicpc.net/problem/15686

# import itertools
#
# # case 1) itertools 사용
# # 입력
# N, M = map(int, input().split())  # N: 도시크기, M: 최대 치킨집 개수
# chicken = []  # 치킨 집 리스트
# house = []    # 집 리스트
# for i in range(N):
#     arr = list(map(int, input().split()))  # 1: 집, 2: 치킨집
#     for j in range(len(arr)):
#         if arr[j] == 2:
#             chicken.append((i, j))
#         elif arr[j] == 1:
#             house.append((i, j))
#
# # step 1) 치킨 집 M개 선택하는 경우의 수
# chicken_arr = list(itertools.combinations(chicken, M))
# result = N*N*len(house)
# for selected in chicken_arr:
#     city_dist = 0
#     # step 2) 해당 치킨집을 기준으로 각 집이 치킨거리 구하기
#     for hx, hy in house:
#         min_dist = N*N
#         for s in selected:
#             min_dist = min(min_dist, abs(hx-s[0])+abs(hy-s[1]))
#         city_dist += min_dist
#     # step 3) 도시의 치킨거리 구하기(최소값)
#     result = min(result, city_dist)
#
# print(result)


# case 2) 조합 구현
def get_city_dist(selected):
    city_dist = 0
    for hx, hy in house:
        min_dist = N*N
        for s in selected:
            min_dist = min(min_dist, abs(hx-s[0])+abs(hy-s[1]))
        city_dist += min_dist
    return city_dist


def combination(selected, start, min_city_dist):
    if len(selected) == M:
        min_city_dist = min(min_city_dist, get_city_dist(selected))
        return min_city_dist

    for i in range(start, len(chicken)):
        x, y = chicken[i]
        min_city_dist = min(min_city_dist, combination(selected+[(x, y)], i+1, min_city_dist))
    return min_city_dist

# 입력
N, M = map(int, input().split())  # N: 도시크기, M: 최대 치킨집 개수
chicken = []  # 치킨 집 리스트
house = []    # 집 리스트
for i in range(N):
    arr = list(map(int, input().split()))  # 1: 집, 2: 치킨집
    for j in range(len(arr)):
        if arr[j] == 2:
            chicken.append((i, j))
        elif arr[j] == 1:
            house.append((i, j))

result = combination([], 0, N*N*len(house))
print(result)