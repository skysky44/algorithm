from collections import deque
T = int(input())
for _ in range(T):
    parenthesis = deque(list(input()))
    stack = []
    while len(parenthesis) > 0:
        p = parenthesis.popleft()
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                stack.append(p)
                break
            else:
                stack.pop()

    if len(parenthesis) == 0 and len(stack) == 0:
        print('YES')
    else:
        print('NO')