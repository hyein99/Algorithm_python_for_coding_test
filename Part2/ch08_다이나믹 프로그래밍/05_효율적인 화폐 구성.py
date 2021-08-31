# 입력
N, M = map(int, input().split())
coin = []            # coin 종류
for _ in range(N):
    coin.append(int(input()))

arr = [M+1]*(M+1)    # arr[x]: x를 만들기 위한 최소 화폐 개수
arr[0] = 0
for i in range(N):
    c = coin[i]
    cnt = 1
    while c <= M:
        arr[c] = min(arr[c], cnt)
        c += coin[i]
        cnt += 1

# 출력
if arr[M] == M+1:
    print(-1)
else:
    print(arr[M])