import sys

sys.setrecursionlimit(10**6)

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(input()))

visited = [[0]*N for _ in range(N)]


def dfs1(y, x, check):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= ny < N) and (0 <= nx < N) and visited[ny][nx] == 0:
            if check == 'B':
                if graph[ny][nx] == 'B':
                    visited[ny][nx] = 1
                    dfs1(ny, nx, check)
            elif check == 'R':
                if graph[ny][nx] == 'R':
                    visited[ny][nx] = 1
                    dfs1(ny, nx, check)
            elif check == 'G':
                if graph[ny][nx] == 'G':
                    visited[ny][nx] = 1
                    dfs1(ny, nx, check)


def dfs2(y, x, check):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= ny < N) and (0 <= nx < N) and visited[ny][nx] == 0:
            if check == 'B':
                if graph[ny][nx] == 'B':
                    visited[ny][nx] = 1
                    dfs2(ny, nx, check)
            else:
                if graph[ny][nx] == 'R' or graph[ny][nx] == 'G':
                    visited[ny][nx] = 1
                    dfs2(ny, nx, check)


cnt_normal = 0
cnt_color_blind = 0

# 색약이 없는 경우
visited = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            cnt_normal += 1
            check = graph[y][x]
            visited[y][x] = 1
            dfs1(y, x, check)

# 색약이 있는 경우
visited = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            cnt_color_blind += 1
            check = graph[y][x]
            visited[y][x] = 1
            dfs2(y, x, check)

print(cnt_normal, cnt_color_blind)
