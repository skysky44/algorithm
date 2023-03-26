import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
# print(graph)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

for i in graph:
    i.sort()

visited = [0]*(N+1)
cnt = 1


def dfs(v):
    global cnt
    visited[v] = cnt

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(R)

for i in visited[1::]:
    print(i)
