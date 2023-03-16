from collections import deque
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    queue = deque(input()[1:-1].split(','))  # 대괄호 제거하기
    flag = 0  # 한 번만 뒤집기
    if n == 0:
        queue = []
    else:
        pass

    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
    else:
        if flag % 2 == 1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
