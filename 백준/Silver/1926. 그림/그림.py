from collections import deque
import sys
sys.setrecursionlimit(10**6)
# 1926
n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
# print(graph)

painting_cnt = 0
max_cnt = 0


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    global cnt
    global painting_cnt
    graph[y][x] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                # print(ny, nx)
                graph[ny][nx] = 0
                cnt += 1
                bfs(ny, nx)


for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            painting_cnt += 1
            cnt = 0
            cnt += 1
            bfs(y, x)
            if cnt > max_cnt:
                max_cnt = cnt

print(painting_cnt)
print(max_cnt)
