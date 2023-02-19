from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque([])
for _ in range(N):
    inp = input().split()
    if len(inp) == 2:
        cmd = inp[0]
        X = int(inp[1])
    else:
        cmd = inp[0]
    if cmd == 'push':
        queue.append(X)
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
