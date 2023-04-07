from collections import deque
# 2644
# 전체 사람 n
n = int(input())
# 촌수 계산 해야하는 서로다른 두사람
p1, p2 = map(int, input().split())
# 부모 자식 관계 수 m
m = int(input())
graph = [[] for i in range(n+1)]
# print(graph)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

cnt = 0
queue = deque([])
visited = [-1]*(n+1)


def bfs(start):
    visited[start] = cnt
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)


bfs(p1)
print(visited[p2])
