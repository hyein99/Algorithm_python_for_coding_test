# # https://programmers.co.kr/learn/courses/30/lessons/60063
#
# import heapq
#
#
# def solution(board):
#     N = len(board)
#
#     def canMove(x1, y1, x2, y2):
#         # (x1, y1), (x2, y2): 이동하려는 위치
#         if 0 <= x1 < N and 0 <= y1 < N and board[x1][y1] == 0:  # (x1, y1)
#             if 0 <= x2 < N and 0 <= y2 < N and board[x2][y2] == 0:  # (x2, y2)
#                 return True
#         return False
#
#     def canSpin(x1, y1, x2, y2):
#         # (x1, y1): 이동하려는 위치, (x2, y2): 대각선
#         if 0 <= x1 < N and 0 <= y1 < N and board[x1][y1] == 0:  # (x1, y1)
#             if board[x2][y2] == 0:
#                 return True
#         return False
#
#     dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     answer = int(1e9)
#     start = [0, (0, 0), (0, 1)]  # 시간, 좌표1, 좌표2
#     qu = []
#     heapq.heappush(qu, start)
#
#     while qu:
#         time, (x1, y1), (x2, y2) = heapq.heappop(qu)
#         # (x1, y1)이 왼쪽 또는 위쪽을 유지
#         if x1 > x2:
#             x1, y1, x2, y2 = x2, y2, x1, y1
#         if y1 > y2:
#             x1, y1, x2, y2 = x2, y2, x1, y1
#
#         # 종료조건
#         if x2 == N - 1 and y2 == N - 1:  # (x2, y2)가 무조건 오른쪽 또는 아래 위치
#             answer = time
#             break
#
#         # 움직일 수 있는 경우의 수
#         # 1) 상하좌우
#         for (dx, dy) in dir:
#             nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
#             if canMove(nx1, ny1, nx2, ny2):
#                 heapq.heappush(qu, [time + 1, (nx1, ny1), (nx2, ny2)])
#         # 2) 가로로 놓여있는 경우
#         if x1 == x2:
#             # 2-1) 축1 기준으로 위로 90도/아래로 90도
#             nx2, ny2, diagx, diagy = x2 - 1, y2 - 1, x1 - 1, y1 + 1
#             if canSpin(nx2, ny2, diagx, diagy):
#                 heapq.heappush(qu, [time + 1, (x1, y1), (nx2, ny2)])
#
#             nx2, ny2, diagx, diagy = x2 + 1, y2 - 1, x1 + 1, y1 + 1
#             if canSpin(nx2, ny2, diagx, diagy):
#                 heapq.heappush(qu, [time + 1, (x1, y1), (nx2, ny2)])
#
#             # 2-2) 축2 기준으로 위로 90도/아래로 90도
#
#         # 2) 가로로 놓여있는 경우
#         else:
#             pass
#             # 2-1) 축1 기준으로 2가지
#             # 2-2) 축2 기준으로 2가지
#
#     return answer