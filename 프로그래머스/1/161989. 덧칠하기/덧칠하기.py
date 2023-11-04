def solution(n, m, section):
    painted = 0
    answer = 0
    for s in section:
        if s > painted:
            painted = s + m - 1
            answer += 1
    return answer