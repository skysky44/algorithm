# N과 M (6)
N, M = map(int, input().split())
nums = map(int, input().split())
sorted_nums = sorted(nums)
stack = []


def backtracking():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(0, N):
        if sorted_nums[i] in stack:
            continue
        elif not stack or sorted_nums[i] > stack[-1]:
            stack.append(sorted_nums[i])
            backtracking()
            stack.pop()


backtracking()
