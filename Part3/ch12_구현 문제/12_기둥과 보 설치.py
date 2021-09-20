# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    def check_install(x, y, a):
        if a == 0:  # 기둥
            # 기둥 조건: 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
            if y == 0 or (x > 0 and 1 in board[x - 1][y]) or 1 in board[x][y] or (y > 0 and 0 in board[x][y - 1]):
                return True
            else:
                return False
        else:  # 보
            # 보 조건: 한쪽 끝이 기둥 위 or 양쪽 끝이 다른 보와 동시에 연결
            # 바닥에 보를 설치하는 경우 없음
            if 0 in board[x][y - 1] or (x < n and 0 in board[x + 1][y - 1]) or (
                    0 < x < n - 1 and 1 in board[x - 1][y] and 1 in board[x + 1][y]):
                return True
            else:
                return False

    def check_remove(x, y, a):
        print('삭제 확인')
        # (x, y)에 a를 삭제하고 구조 확인
        board[x][y].remove(a)
        # (x, y)에 영향을 받는 구간 확인
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx <= n and 0 <= ny <= n:
                for i in board[nx][ny]:
                    if not check_install(nx, ny, i):
                        board[x][y].append(a)
                        return False
        board[x][y].append(a)
        return True

    # board: 기둥(0)과 보(1)를 이용한 벽면 구조
    board = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    # 중심, 왼쪽, 왼쪽위대각선, 위, 오른쪽
    dir = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 0)]
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            if check_install(x, y, a):
                board[x][y].append(a)
            else:
                continue
        else:  # 삭제
            if check_remove(x, y, a):
                board[x][y].remove(a)
            else:
                continue

    # 최종 구조물 상태
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if len(board[x][y]) == 2:
                answer.extend([[x, y, 0], [x, y, 1]])
            elif len(board[x][y]) == 1:
                answer.append([x, y, board[x][y][0]])
    return answer