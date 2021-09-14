# 팀 합치기: 두 팀을 합치는 연산
# 같은 팀 여부 확인: 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산

## case 1: find, union 활용
def find_parent(x):
    if team[x] != x:
        team[x] = find_parent(team[x])
    return team[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

# 입력
N, M = map(int, input().split())
team = [i for i in range(N)]
for _ in range(M):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(a-1, b-1)
    else:
        if find_parent(a-1) == find_parent(b-1):
            print("YES")
        else:
            print("NO")


## case 2: team 다 검사하기
# def merge_team(a, b):
#     if a < b:     # b를 a로
#         past = team[b]
#         new = team[a]
#         for i in range(len(team)):
#             if team[i] == past:
#                 team[i] = new
#
#
# def check_team(a, b):
#     if team[a] == team[b]:
#         return 'YES'
#     else:
#         return 'NO'
#
# # 입력
# N, M = map(int, input().split())
# team = [i for i in range(N)]
# for _ in range(M):
#     x, a, b = map(int, input().split())
#     if x == 0:
#         merge_team(a-1, b-1)
#     else:
#         print(check_team(a-1, b-1))