import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

visited = [-1]*(N+1)


def dfs(v, depth):
    visited[v] = depth

    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = depth
            dfs(i, depth+1)


dfs(R, 0)

for i in visited[1::]:
    print(i)
