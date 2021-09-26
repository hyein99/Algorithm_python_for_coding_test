# https://www.acmicpc.net/problem/14888

maxresult = -int(1e9)
minresult = int(1e9)

def putOperation(idx, result):
    global maxresult, minresult

    if idx == N:
        # 계산 후 최댓값, 최솟값 갱신
        maxresult = max(maxresult, result)
        minresult = min(minresult, result)
        return

    for j in range(4):
        if op[j] > 0:
            op[j] -= 1
            if j == 0:    # 덧셈
                putOperation(idx+1, result+arr[idx])
            elif j == 1:  # 뺄셈
                putOperation(idx+1, result-arr[idx])
            elif j == 2:  # 곱셈
                putOperation(idx+1, result*arr[idx])
            else:         # 나눗셈
                if result < 0:
                    putOperation(idx+1, (-result)//arr[idx]*(-1))
                else:
                    putOperation(idx+1, result//arr[idx])
            op[j] += 1


# 입력
N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

putOperation(1, arr[0])

# 출력(최댓값, 최솟값)
print(maxresult)
print(minresult)