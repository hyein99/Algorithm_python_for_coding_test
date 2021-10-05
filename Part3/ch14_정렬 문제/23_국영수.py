# https://www.acmicpc.net/problem/10825

N = int(input())
grades = []
for _ in range(N):
    names, k, e, m = input().split()
    grades.append((names, int(k), int(e), int(m)))

grades.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(grades[i][0])