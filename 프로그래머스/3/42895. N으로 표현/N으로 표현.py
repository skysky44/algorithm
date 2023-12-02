def solution(N, number):
    dp = []

    for i in range(1, 9):
        case = set()
        case.add(int(str(N) * i))
        for j in range(0, i - 1):  # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for a in dp[j]:
                for b in dp[-1 - j]:
                    case.add(a - b)
                    case.add(a + b)
                    case.add(a * b)
                    if b != 0:
                        case.add(a // b)

        if number in case:
            answer = i
            break
        dp.append(case)
    else:
        answer = -1
    return answer
