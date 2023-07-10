# 스택 수열


import sys
input = sys.stdin.readline
n = int(input())
stack = []
cnt = 1
answer = []
for _ in range(n):
    num = int(input())
    while num >= cnt:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    for i in answer:
        print(i)
