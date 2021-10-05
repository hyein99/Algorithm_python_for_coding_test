# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stages.sort()
    fail = []
    idx = 0
    for i in range(1, N + 1):
        cnt = 0
        if idx >= len(stages):  # 예외 케이스([1, 1, 1, 1, 1])
            fail.append((i, 0))
            continue

        while stages[idx + cnt] == i:
            cnt += 1
            if idx + cnt >= len(stages):
                break
        if len(stages) - idx == 0:
            frate = 0
        else:
            frate = cnt / (len(stages) - idx)
        fail.append((i, frate))
        idx += cnt

    fail.sort(key=lambda x: (-x[1], x[0]))

    return [x[0] for x in fail]

# def soluti1on(N, stages):
#     slist = [0 for _ in range(N + 1)]
#     for n in stages:
#         for i in range(n):
#             slist[i] += 1
#     frate = [[i, 0] for i in range(1, len(slist))]
#     for j in range(1, len(slist)):
#         if slist[j - 1] == 0:
#             break
#         frate[j - 1][1] = (slist[j - 1] - slist[j]) / slist[j - 1]
#     frate.sort(key=lambda x: (-x[1], x[0]))
#
#     return [x[0] for x in frate]
