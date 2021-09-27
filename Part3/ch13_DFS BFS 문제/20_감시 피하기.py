# https://www.acmicpc.net/problem/18428

def solution():
    for i in range(len(blank)):
        graph[blank[i][0]][blank[i][1]] = 'O'
        for j in range(i+1, len(blank)):
            graph[blank[j][0]][blank[j][1]] = 'O'
            for k in range(j+1, len(blank)):
                graph[blank[k][0]][blank[k][1]] = 'O'
                if avoidable():
                    return 'YES'
                graph[blank[k][0]][blank[k][1]] = 'X'
            graph[blank[j][0]][blank[j][1]] = 'X'
        graph[blank[i][0]][blank[i][1]] = 'X'

    return 'NO'


def avoidable():
    for t in teacher:
        for d in dir:
            (tx, ty) = t
            tx += d[0]
            ty += d[1]
            while 0<=tx<N and 0<=ty<N:
                if graph[tx][ty] == 'S':
                    return False
                elif graph[tx][ty] == 'O':
                    break
                tx += d[0]
                ty += d[1]
    return True

# 입력
N = int(input())
graph = []  # N*N
# 선생님 수: 5이하의 자연수, 전체 학생수: 30이하 자연수, 빈칸: 3개 이상
for _ in range(N):
    graph.append(list(input().split()))  # S학생, T선생, X

# 선생님 위치와 빈칸 위치 저장하기
teacher, blank = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == 'X':
            blank.append((i, j))
dir = [(1,0), (-1,0), (0,1), (0,-1)]

# 장애물 3개 세우는 경우의 수 구하기
print(solution())
