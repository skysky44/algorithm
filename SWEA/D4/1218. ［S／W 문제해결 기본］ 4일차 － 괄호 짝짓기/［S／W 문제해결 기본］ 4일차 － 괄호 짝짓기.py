# import sys
from collections import deque
# sys.stdin = open("input.txt")
for i in range(10):
    T = int(input())
    print(f'#{i+1}', end=' ')
    bracket = deque(list(input()))
    check = deque([])
    for i in range(T):
        a = bracket.popleft()
        if a in ['(', '[', '{', '<']:
            check.append(a)
        elif a in [')', ']', '}', '>']:
            try:
                if (check.pop() + a) in ['()', '[]', '{}', '<>']:
                    pass
                else:
                    print(0)
                    break
            except:
                print(0)
                break
        else:
            print(0)
            break
    else:
        if len(check) == 0:
            print(1)
        else:
            print(0)
