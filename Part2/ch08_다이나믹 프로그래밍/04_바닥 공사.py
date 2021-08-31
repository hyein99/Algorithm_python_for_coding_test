N = int(input())

x, y = 1, 3
for i in range(3, N+1):
    x, y = y, 2*x+y
print(y%796796)