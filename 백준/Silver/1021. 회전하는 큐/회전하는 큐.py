from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
queue = deque([n for n in range(1, n+1)])
nums = list(map(int, input().split()))
for i in nums:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) > len(queue)//2:
                while True:
                    queue.appendleft(queue.pop())
                    cnt += 1
                    if queue[0] == i:
                        break
            else:
                while True:
                    queue.append(queue.popleft())
                    cnt += 1
                    if queue[0] == i:
                        break
print(cnt)
