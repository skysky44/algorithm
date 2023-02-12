import sys
input= sys.stdin.readline
from collections import deque
nums = deque()
N = int(input())
for _ in range(N):
    cmd_input = input().split()
    if len(cmd_input) == 1:
        cmd = cmd_input[0]
    else:
        cmd = cmd_input[0]
        x = cmd_input[1]

    if cmd == 'push_front':
        nums.appendleft(x)
    elif cmd == 'push_back':
        nums.append(x)
    elif cmd == 'pop_front':
        if nums:
            print(nums.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if nums:
            print(nums.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(nums))
    elif cmd == 'empty':
        if nums:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if nums:
            print(nums[0])
        else:
            print(-1)
    elif cmd == "back":
        if nums:
            print(nums[-1])
        else:
            print(-1)
