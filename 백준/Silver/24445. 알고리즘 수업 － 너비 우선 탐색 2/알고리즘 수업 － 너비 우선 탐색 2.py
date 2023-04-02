from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R
graph = [[] for _ in range(N+1)]
# print(graph)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)


for u in graph:
    u.sort(reverse=True)
# 내림 차순 방문
#  V : 정점 집합, E : 간선 집합, R : 시작 정점


def bfs(R):
    queue = deque([])
    visited = [False]*(N+1)
    cnt = 1
    visited[R] = cnt
    queue.append(R)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v] == False:
                cnt += 1
                visited[v] = cnt
                queue.append(v)

    for i in visited[1::]:
        if i == False:
            print(0)
        else:
            print(i)


bfs(R)

