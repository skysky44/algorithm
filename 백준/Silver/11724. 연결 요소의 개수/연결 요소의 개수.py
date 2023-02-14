import sys
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    grid[x].append(y)
    grid[y].append(x)

visited = [False]*(N+1)
visited[0] = True
cnt = 0
for n in range(1, N+1):
    if visited[n] == False:
        cnt += 1
        start = n
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for i in grid[cur]:
            if not visited[i] == True:
                visited[i] = True
                stack.append(i)
print(cnt)
