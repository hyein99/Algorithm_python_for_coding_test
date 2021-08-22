# 입력
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 풀이 2)
arr.sort()
first = arr[-1]
second = arr[-2]

cnt = M // (K+1)
result = cnt * (first*K+second)

if M % (K+1):
    result += first + second * (M % (K+1))

print(result)


# 풀이 1)
# arr.sort()
# first = arr[-1]
# second = arr[-2]
#
# result = 0
# while True:
#     if M == 0:
#         break
#     if M >= K:
#         result += first*K
#         M -= K
#     if M > 0:
#         result += second
#         M -= 1
# print(result)