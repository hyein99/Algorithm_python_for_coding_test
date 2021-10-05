# https://www.acmicpc.net/problem/18310

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr[(N+1)//2 - 1])