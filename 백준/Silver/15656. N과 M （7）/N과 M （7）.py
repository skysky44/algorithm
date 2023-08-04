# N과 M (7)
N, M = map(int, input().split())
nums = map(int, input().split())
sorted_nums = sorted(nums)
stack = []


def backtracking():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(0, N):
        stack.append(sorted_nums[i])
        backtracking()
        stack.pop()


backtracking()
