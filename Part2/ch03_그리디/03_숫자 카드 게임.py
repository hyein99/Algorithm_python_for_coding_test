# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

# 입력
N, M = map(int, input().split())
result = 0
for i in range(N):
    arr = list(map(int, input().split()))
    result = max(result, min(arr))

print(result)
