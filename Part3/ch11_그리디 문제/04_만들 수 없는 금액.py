# 현재 상태: 1부터 Target-1 까지의 모든 금액을 만들 수 있는 상태
# 현재 확인 하는 동전의 단위가 Target 이하인지 체크
# 만약 해당금액을 만들 수 있다면, Target 값 업데이트

# 입력
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for a in arr:
    if target < a:  # 확인 한느 동전 단위가 target보다 크면 target 만들 수 없음
        break
    target += a

print(target)