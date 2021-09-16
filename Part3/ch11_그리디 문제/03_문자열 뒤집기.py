# 0011001100 > 정답 2, switch: 4
# 000111000111 > 정답 2, switch: 3

# 입력
S = list(map(int, list(input())))

cnt = 1
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        cnt += 1

print(cnt//2)


