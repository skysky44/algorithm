from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
que = deque()
for _ in range(N):
    inp = list(input().split())
    if len(inp) == 2:
        cmd, x = inp[0], inp[1]
    else:
        cmd = inp[0]

    if cmd == 'push':
        que.append(x)
    elif cmd == 'pop':
        try:
            print(que.popleft())
        except:
            print(-1)
    elif cmd == 'size':
        print(len(que))
    elif cmd == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        try:
            print(que[0])
        except:
            print(-1)
    elif cmd == 'back':
        try:
            print(que[-1])
        except:
            print(-1)