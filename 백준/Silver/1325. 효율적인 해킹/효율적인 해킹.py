import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_count = 0
result = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    stack = [i]
    count = 0

    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = True
            count += 1
            stack.extend(graph[cur])

    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)

