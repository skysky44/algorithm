from collections import deque
import sys
input = sys.stdin.readline

t = int(input())


def bfs(start, plane):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        if visited.count(True) == n:  # 모든 국가를 방문 하면 끝
            return plane

        cur = q.popleft()

        for c in graph[cur]:
            if not visited[c]:
                q.append(c)
                plane += 1
                visited[c] = True


for _ in range(t):
    n, m = map(int, input().split())
    visited = [False] * (n+1)

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    p = bfs(1, 0)
    print(p)
