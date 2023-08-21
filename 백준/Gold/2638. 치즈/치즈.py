import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
time = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = 1  # 0,0에 치즈가?

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:  # 0 이거나 방문 안했으면 다음 방문할 예정
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:  # 치즈라면 방문 횟수 1 추가
                    visited[nx][ny] += 1

    melted = []  # 녹아야 될 치즈
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:  # bfs로 두 번 이상 방문한 치즈
                melted.append((i, j))

    return melted


while True:
    melted = bfs()

    if not melted:  # 더 이상 녹을 치즈 없으면 멈춤
        break

    time += 1  # 녹아 없어지는데 걸리는 시간 추가

    for x, y in melted:  # 치즈 녹이고 공기로 바꾸기
        graph[x][y] = 0

print(time)
