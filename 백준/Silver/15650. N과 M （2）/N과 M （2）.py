# N과 M (2)
N, M = map(int, input().split())
# nums = [i for i in range(1, N+1)]
stack = []


def backtracking():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N+1):
        if i in stack:
            continue
        elif not stack or i > stack[-1]:
            stack.append(i)
            backtracking()
            stack.pop()


backtracking()
