# import sys
from collections import deque
# sys.stdin = open("input.txt")
for _ in range(10):
    T = int(input())
    nums = map(int, input().split())
    stack = deque(nums)
    while True:
        for i in range(1, 6):
            temp = (stack.popleft())-i
            if temp <= 0:
                temp = 0
                stack.append(temp)
                break
            else:
                stack.append(temp)
        if stack[-1] == 0:
            break
    print(f'#{T}', end=' ')
    print(*stack)
