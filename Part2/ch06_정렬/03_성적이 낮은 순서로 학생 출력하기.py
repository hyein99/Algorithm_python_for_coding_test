# 입력
N = int(input())
arr = []
for _ in range(N):
    name, grade = input().split()
    arr.append((name, int(grade)))

arr.sort(key=lambda x: x[1])
for i in range(N):
    print(arr[i][0], end=' ')