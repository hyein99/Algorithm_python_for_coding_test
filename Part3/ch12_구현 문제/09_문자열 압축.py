# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    def compress(n):
        compressed = ''
        i = 0
        cnt = 1
        sub_s = ''
        while i + n <= len(s):
            if s[i:i + n] == sub_s:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + sub_s
                else:
                    compressed += sub_s
                sub_s = s[i:i + n]
                cnt = 1
            i += n
        # 마지막에 처리못한 부분
        if cnt > 1:
            compressed += str(cnt) + sub_s
        else:
            compressed += sub_s
        # n으로 나누어떨어지지 않는 경우
        if i < len(s):
            compressed += s[i:]

        return len(compressed)

    minS = len(s)
    for i in range(1, len(s) // 2 + 1):
        minS = min(minS, compress(i))

    return minS