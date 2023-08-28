import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
space = []
for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        j = temp.index(9)
        start = (i, j)
    space.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
size = 2

def bfs(start, space, size):
    q = deque()
    q.append(start)

    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    targets = []
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if space[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if 0 < space[nx][ny] < size:
                        targets.append((nx, ny, distance[nx][ny]))

    return sorted(targets, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
time = 0
while True:
    shark = bfs(start, space, size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()
    
    time += dist
    space[start[0]][start[1]], space[nx][ny] = 0, 0
    start = (nx, ny)  # 아기 상어의 위치를 업데이트
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(time)
