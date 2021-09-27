# https://www.acmicpc.net/problem/16234

def solution():
    days = 0
    # step 1) 국경선 공유할 수 있는 나라 체크하여 union에 표시
    # step 2) 연합하는 나라끼리 인구이동
    # step 3) 연합할 수 있는 나라 없으면 종료
    # 연합을 이루고 있는 각 칸 인구수 = (연합 인구수)/칸수 (소수점 버림)
    while True:
        union = [[0] * N for _ in range(N)]  # 연합 팀 표시
        cnt = 1    # 연합 팀 번호
        team = []  # 연합 팀 구성
        psum = 0   # 인구이동할 인구 수
        for i in range(N):
            for j in range(N):
                if union[i][j] == 0:  # 아직 연합이 정해지지 않은 곳
                    x, y = i, j
                    for (dx, dy) in dir:
                        nx, ny = x+dx, y+dy
                        # 연합 조건: 범위내,

        days += 1
    return days


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
dir = [(1,0), (0,1) (-1,0), (0,-1)]

# 출력
print(solution())