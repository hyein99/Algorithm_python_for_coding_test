from collections import Counter

# 입력
N, M = map(int, input().split())  # 볼링공 개수, 최대 무게
arr = list(map(int, input().split()))

result = 0
arr_cnt = Counter(arr)
for i in range(1, M+1):
    a = arr_cnt[i]  # A가 i무게를 선택하는 경우의 수
    N -= a          # B가 선택하는 경우의 수
    result += a*N

print(result)
