# https://programmers.co.kr/learn/courses/30/lessons/60062
# 시계 혹은 반시계 방향으로 외벽 따라 이동
# 외벽: n, 취약지점 위치: weak, 각 친구가 1시간동안 이동할 수 있는 거리: dist
# 취약 지점을 점검하기 위해 보내야하는 친구 수의 최소값 리턴

import itertools


def solution(n, weak, dist):
    answer = len(dist) + 1

    # step 1) 원을 길이를 2배로 늘려 일자로 변경
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # step 2) 친구 배치 순서(permutations)
    friends_arr = list(itertools.permutations(dist, len(dist)))
    for friends in friends_arr:
        # step 3) 시작 취약점 위치
        for idx in range(length):
            # 모든 취약점을 점검하기 위해 몇명이 필요한지
            cnt = 0  # 투입 인원수
            start, end = idx, idx + length - 1
            position = weak[start]
            while cnt < len(dist):
                cnt += 1
                position += friends[cnt - 1]
                if position >= weak[end]:
                    answer = min(answer, cnt)  # 최소 몇명인지
                    break

                while weak[start] <= position:
                    start += 1
                position = weak[start]

    # 모두 투입해도 점검할 수 없는 경우
    if answer > len(dist):
        return -1

    return answer