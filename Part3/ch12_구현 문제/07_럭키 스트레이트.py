# 럭키 스트레이트
# 자릿수를 기준으로 N을 반으로 나누어 왼쪽 부분의 자릿수 합과 오른쪽 자릿수합이 동일한 상황

# 입력
N = list(map(int, list(input())))

left, right = 0, 0
for i in range(len(N)//2):
    left += N[i]
    right += N[i+len(N)//2]

if left == right:
    print('LUCKY')
else:
    print('READY')