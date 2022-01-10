# N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 최대한 많이 나누기

# 입력
N, K = map(int, input().split())

cnt = 0
while N != 1:
    if N%K:
        N -= 1
    else:
        N /= K
    cnt += 1

print(cnt)