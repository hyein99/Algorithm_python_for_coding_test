# 입력
N, M = map(int, input().split())
result = 0
for i in range(N):
    arr = list(map(int, input().split()))
    result = max(result, min(arr))

print(result)
