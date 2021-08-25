# 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))

def cut(height):
    cnt = 0
    for a in arr:
        cnt += max(0, a-height)
    return cnt

def bin_search(target):
    start, end = 0, max(arr)
    while start <= end:
        mid = (start+end)//2
        cnt = cut(mid)
        if cnt >= target: # 높이를 높여서 덜 잘라야 함
            start = mid+1
        else: # 높이를 낮춰서 더 잘라야 함
            end = mid-1
    return end

print(bin_search(6))