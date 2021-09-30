# https://www.acmicpc.net/problem/16234

from collections import deque

def solution():
    global visited

    days = 0
    while True:
        tnum = 1  # 연합팀 번호(연합팀 개수를 의미)

        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:  # 연합팀이 정해지지 않은 곳만 방문
                    dfs(i, j, tnum)
                    tnum += 1

        # 종료조건: 연합할 수 없는 나라가 없는 경우
        if tnum > N*N:
            break

        visited = [[0] * N for _ in range(N)]  # 방문 여부 초기화
        days += 1
    return days


def dfs(i, j, tnum):
    # tnum 번째 연합 생성
    team = [(i, j)]
    tsum = population[i][j]
    qu = deque()
    qu.append((i, j))

    while qu:
        x, y = qu.pop()
        visited[x][y] = tnum
        for (dx, dy) in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 범위내에 있고 방문하지 않은 곳
                if canUnite(population[x][y], population[nx][ny]):
                    qu.append((nx, ny))
                    visited[nx][ny] = tnum
                    team.append((nx, ny))
                    tsum += population[nx][ny]

    # tnum 번째 연합 인구이동
    tpop = tsum // len(team)
    for (x, y) in team:
        population[x][y] = tpop


def canUnite(a, b):
    # 국경선을 공유하는 두 나라 인구 차이가 L 이상 R 이하면 국경선 개방
    if L <= abs(a-b) <= R:
        return True
    else:
        return False


# 입력
N, L, R = map(int, input().split())
population = []
for _ in range(N):
    population.append(list(map(int, input().split())))

dir = [(1,0), (0,1), (-1,0), (0,-1)]   # 방향
visited = [[0] * N for _ in range(N)]  # 방문여부

# 출력
print(solution())

