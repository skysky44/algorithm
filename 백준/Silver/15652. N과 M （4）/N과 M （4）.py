# N과 M (4)
N, M = map(int, input().split())
stack = []


def backtracking():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N+1):
        if not stack or i >= stack[-1]:
            stack.append(i)
            backtracking()
            stack.pop()


backtracking()
