import sys
input = sys.stdin.readline

N = int(input())
stack = []
for n in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
