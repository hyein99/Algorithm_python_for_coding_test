
# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    qu = []
    # heapq에 삽입
    for i in range(len(food_times)):
        heapq.heappush(qu, (food_times[i], i + 1))

    total = 0                 # 먹기 위해 사용한 시간
    prev = 0                  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수
    while total + (qu[0][0]-prev)*length <= k:
        now = heapq.heappop(qu)[0]
        total += (now-prev) * length
        length -= 1
        prev = now

    # 남은 음식 들 중에 몇 번째 음식인가
    result = sorted(qu, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k-total) % length][1]


# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     qu = []
#     # heapq에 삽입
#     for i in range(len(food_times)):
#         heapq.heappush(qu, (food_times[i], i + 1))
#
#     left = len(food_times)  # 남은 음식 개수
#     time, num = heapq.heappop(qu)  # 제일 시간이 짧은 음식 pop
#     while left * time < k:
#         k -= left * time
#         for i in range(len(food_times)):
#             if food_times[i] > 0:
#                 food_times[i] -= time
#             if food_times[i] > 0:
#                 heapq.heappush(qu, (food_times[i], i + 1))
#         left -= 1
#         time, num = heapq.heappop(qu)
#
#     turn = 0
#     while k:
#         if food_times[turn] > 0:
#             food_times[turn] -= 1
#             k -= 1
#         turn = (turn + 1) % len(food_times)
#
#     return turn + 1

print(solution([2, 3, 4, 1, 2], 10))