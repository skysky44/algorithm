import sys
input = sys.stdin.readline
stack = []
string = input().strip()
target = input().strip()
for s in string:
    stack.append(s)
    if target[-1] == s:
        if stack[-len(target):] == list(target):
            for _ in range(len(target)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print(*stack, sep="")
