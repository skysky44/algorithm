import sys
sys.setrecursionlimit(10**6)
# 가로 M 세로 N


def dfs(y, x):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= ny <= N-1) and (0 <= nx <= M-1) and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(ny, nx)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    cnt = 0
    # print(graph)
    for i in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    # print(graph)

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                graph[y][x] = 0
                cnt += 1
                dfs(y, x)
    print(cnt)
