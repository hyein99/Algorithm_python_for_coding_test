# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향 x
# 자물쇠 영역 내에서는 key 돌기(1)와 lock 홈(0) 정확히 일치
# 열쇠의 돌기와 자물쇠 돌기 만나면 안됨
# 열쇠 크기는 자물쇠 크기보다 작거나 같음
# 0: 홈, 1: 돌기

def solution(key, lock):
    # 키가 자물쇠에 부합하는지 판단하는 함수
    def compare(key, lock):
        for i in range(len(lock)):
            for j in range(len(lock)):
                if lock[i][j] == key[i][j]:
                    return False
        return True

    # 키를 회전하여 자물쇠와 비교
    rotated = []
    rotated.append([[key[j][i] for i in range(len(key))] for j in range(len(key))])
    rotated.append([[key[i][j] for i in range(len(key) - 1, -1, -1)] for j in range(len(key))])
    rotated.append([[key[i][j] for i in range(len(key) - 1, -1, -1)] for j in range(len(key) - 1, -1, -1)])
    rotated.append([[key[i][j] for i in range(len(key))] for j in range(len(key) - 1, -1, -1)])

    print(rotated)

    # 90도 회전
    # 좌우 이동
    # 상하 이동

    answer = True
    return answer