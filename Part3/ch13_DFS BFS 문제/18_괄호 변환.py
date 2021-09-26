# 문자열을 u, v로 분리하는 함수
def splitString(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            break

    return s[:i + 1], s[i + 1:]


# 올바른 괄호 문자열인지 판단하는 함수
def isCorrect(s):
    qu = []
    for c in s:
        if not qu:
            if c == ')':  # ')'
                return False
            else:  # '('
                qu.append('(')
        else:
            if c == '(':  # '(('
                qu.append('(')
            else:  # '()'
                qu.pop()

    if qu:
        return False
    return True


# 괄호 방향을 뒤집는 함수
def reverseString(s):
    result = ''
    for c in s:
        if c == ')':
            result += '('
        else:
            result += ')'
    return result


def solution(p):
    # 1. 입력이 빈 문자열인 경우 빈 문자열 반환
    if not p:
        return ''

    # 2. "균형잡힌 괄호 문자열" u, v로 분리
    # u: 더 이상 분리할 수 없음, v: 빈 문자열이 될 수 있음
    u, v = splitString(p)

    # 3. u가 "올바른 괄호 문자열" 이라면 v에 대해 1단계부터 다시 수행
    # 수행 결과를 u에 이어 붙인 후 반환
    if isCorrect(u):
        return u + solution(v)
    # 4. u가 "올바른 괄호 문자열"이 아닌 경우
    else:
        return '(' + solution(v) + ')' + reverseString(u[1:-1])
