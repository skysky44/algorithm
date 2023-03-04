import sys
input = sys.stdin.readline
n = int(input())
stack = []
cnt = 1
answer = []
for _ in range(n):
    input_num = int(input())
    while input_num >= cnt:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == input_num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    for i in answer:
        print(i)
