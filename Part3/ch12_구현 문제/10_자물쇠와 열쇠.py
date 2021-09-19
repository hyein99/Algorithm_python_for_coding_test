# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향 x
# 자물쇠 영역 내에서는 key 돌기(1)와 lock 홈(0) 정확히 일치
# 열쇠의 돌기와 자물쇠 돌기 만나면 안됨
# 열쇠 크기는 자물쇠 크기보다 작거나 같음
# 0: 홈, 1: 돌기

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 키를 90도 회전하는 함수
    def rotate90(key):
        return [[key[j][i] for j in range(M)] for i in range(M - 1, -1, -1)]

    # 키가 자물쇠에 부합하는지 판단하는 함수
    def compare(newlock):
        for i in range(N, 2 * N):
            for j in range(N, 2 * N):
                if newlock[i][j] != 1:
                    return False
        return True

    # step 1) 자물쇠 크기를 3배하기(상하좌우이동)
    newlock = [[0 for _ in range(3 * N)] for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            newlock[N + i][N + j] = lock[i][j]

    # step 2) 4가지 방향으로 회전
    for _ in range(4):
        key = rotate90(key)
        for x in range(N * 2):
            for y in range(N * 2):
                # 자물쇠(newlock)에 열쇠(key) 넣기
                for i in range(M):
                    for j in range(M):
                        newlock[x + i][y + j] += key[i][j]
                # 열쇠가 맞는지 확인
                if compare(newlock):
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(M):
                    for j in range(M):
                        newlock[x + i][y + j] -= key[i][j]
    return False
