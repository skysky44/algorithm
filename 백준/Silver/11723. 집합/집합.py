import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    cmd = list(map(str, input().split()))
    if len(cmd) == 1:
        if cmd[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        c, x = cmd[0], cmd[1]
        x = int(x)

        if c == "add":
            S.add(x)
        elif c == "remove":
            S.discard(x)
        elif c == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
