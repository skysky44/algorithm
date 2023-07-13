# 토마토
from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())

# M 상자 가로, N 상자 세로, H 높이
# 1 익은 것, 0 익지 않은 것, -1 토마토 없음

# 3차원 그래프 만들기
graph_3D = []
for _ in range(H):
    graph_2D = []
    for _ in range(N):
        graph_2D.append(list(map(int, input().split())))
    graph_3D.append(graph_2D)

# print(graph_3D)

queue = deque([])  # 큐 초기화
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토 위치를 큐에 추가

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph_3D[i][j][k] == 1:
                queue.append((i, j, k))

# BFS


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if graph_3D[nz][nx][ny] == 0:
                    graph_3D[nz][nx][ny] = graph_3D[z][x][y] + 1
                    queue.append((nz, nx, ny))


bfs()


# print(graph_3D)
# 모든 토마토가 익지 않은 경우에는 -1, 그 외에는 최대 일 출력
max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph_3D[i][j][k] == 0:
                print(-1)
                exit()
            max_day = max(max_day, graph_3D[i][j][k])

print(max_day - 1)  # 처음 익은 토마토를 1일로 치기 때문에 -1을 해줍니다.
