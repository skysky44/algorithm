from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    index_queue = deque([n for n in range(len(queue))])
    cnt = 1
    while True:
        temp = queue[0]
        temp_index = index_queue[0]
        if temp == max(queue):
            if temp_index == m:
                break
            else:
                queue.popleft()
                index_queue.popleft()
                cnt += 1
        else:
            queue.append(queue.popleft())
            index_queue.append(index_queue.popleft())
    print(cnt)
