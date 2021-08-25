# 입력
# N = int(input())
# narr = list(map(int, input().split()))
# M = int(input())
# marr = list(map(int, input().split()))

# 풀이 1: 이진 탐색
# def bin_search(arr, target):
#     start, end = 0, len(arr)-1
#     while start < end:
#         mid = (start+end)//2
#         if arr[mid] == target:
#             return 'yes'
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 'no'
#
# for m in marr:
#     print(bin_search(narr, m), end = ' ')


# 풀이 2: 계수 정렬
# cnt = [0]*1000001
# for n in narr:
#     cnt[n] += 1
#
# for m in marr:
#     if cnt[m]:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


# 풀이 3: 집합 자료형 이용
# 입력
N = int(input())
narr = set(map(int, input().split()))
M = int(input())
marr = list(map(int, input().split()))

for m in marr:
    if m in narr:
        print('yes', end=' ')
    else:
        print('no', end=' ')