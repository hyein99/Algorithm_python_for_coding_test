# 입력
N = int(input())
arr = list(map(int, input().split()))

arr[1] = max(arr[0], arr[1])
for i in range(2, N):
    arr[i] = max(arr[i-1], arr[i-2]+arr[i])
print(arr[N-1])