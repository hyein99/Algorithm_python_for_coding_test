# 입력
N = int(input())
scared = list(map(int, input().split()))

scared.sort()
result = 0    # 그룹 수
cnt = 0       # 현재 그룹에 포함된 모험가 수
for i in range(len(scared)):
    cnt += 1
    if scared[i] <= cnt:
        cnt = 0
        result += 1

print(result)