def solution(p):

    if p == '':
        return p

    left_cnt = 0
    right_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        elif p[i] == ')':
            right_cnt += 1
        if left_cnt == right_cnt:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    # 균형 잡힌 문자열인지 확인
    if balance(u):
        converted_v = solution(v)
        return u + converted_v
    else:
        new_string = '('
        new_string += solution(v)
        new_string += ')'
        u = u[1:len(u) - 1]  # u의 첫 번째와 마지막 문자를 제거
        for char in u:  # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
            if char == '(':
                new_string += ')'
            else:
                new_string += '('
        return new_string

# 함수를 여러개 사용.

# 균형 잡힌 괄호 문자열 확인


def balance(p):
    stack = []
    for char in p:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return True
