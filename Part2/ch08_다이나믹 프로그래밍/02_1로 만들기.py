from collections import defaultdict

X = int(input())

dic = defaultdict(int)
def makeOne(N):
    for i in range(2, N+1):
        dic[i] = dic[i-1]+1
        if i%2 == 0:
            dic[i] = min(dic[i], dic[i//2]+1)
        if i%3 == 0:
            dic[i] = min(dic[i], dic[i//3]+1)
        if i%5 == 0:
            dic[i] = min(dic[i], dic[i//5]+1)
    return dic[N]

print(makeOne(X))