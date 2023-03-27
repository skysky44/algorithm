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

# i번 노드의 깊이 di 노드의 방문순서 ti

visited = [[-1, 0]]*(N+1)
turn = 1


def dfs(r, depth):
    global turn

    visited[r] = depth * turn
    # print(visited[r])
    # print(visited)
    for i in graph[r]:
        if visited[i] == [-1, 0]:
            turn += 1
            dfs(i, depth+1)


dfs(R, 0)

result = 0

for i in visited[1::]:
    if i == [-1, 0]:
        result += 0
    else:
        result += i
print(result)