# 0, 1의 경우 더하기가 효율적

# 입력
S = list(map(int, list(input())))

result = S[0]
for i in range(1, len(S)):
    if S[i] <= 1 or result <= 1:
        result += S[i]
    else:
        result *= S[i]
print(result)