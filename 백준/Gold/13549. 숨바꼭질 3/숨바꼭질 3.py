from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
stack = deque([N])
visited[N] = 0

while stack:
    cur = stack.popleft()
    if cur == K:
        print(visited[cur])
        break
    for i in (cur * 2, cur - 1, cur + 1):
        if 0 <= i <= 100000 and visited[i] == -1:
            if i == (cur * 2):
                visited[i] = visited[cur]
                stack.appendleft(i)
                
            else:
                visited[i] = visited[cur] + 1
                stack.append(i)