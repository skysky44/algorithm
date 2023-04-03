from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R
graph = [[] for _ in range(N+1)]


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for u in graph:
    u.sort()
# 오름 차순 방문
#  V : 정점 집합, E : 간선 집합, R : 시작 정점


def bfs(R):
    queue = deque([])
    visited_depth = [-1]*(N+1)
    visited_cnt = [0]*(N+1)
    depth = 0
    cnt = 1
    visited_depth[R] = depth
    visited_cnt[R] = cnt
    queue.append(R)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if visited_cnt[v] == 0:
                cnt += 1
                visited_cnt[v] = cnt
                visited_depth[v] = visited_depth[u] + 1  # 이전 정점 깊이 +1
                queue.append(v)

    result = 0
    for i in range(1, N+1):
        result += (visited_depth[i]*visited_cnt[i])
    print(result)


bfs(R)
