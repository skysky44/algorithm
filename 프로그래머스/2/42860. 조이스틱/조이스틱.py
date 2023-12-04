def solution(name):
    alpha_cnt = 0
    cursor_cnt = len(name) - 1  # 최소 이동 횟수는 길이 - 1

    for i, alpha in enumerate(name):
        alpha_cnt += min(ord(alpha) - 65, 91 - ord(alpha))  # 위로 or 아래로 최솟값

        # 해당 알파벳 다음부터 연속된 A
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 기본 최소 길이, 연속된 A의 왼쪽시작, 연속된 A의 오른쪽시작 비교
        cursor_cnt = min(
            [cursor_cnt, 2 * i + len(name) - next, i + 2 * (len(name) - next)]
        )

    answer = cursor_cnt + alpha_cnt
    return answer