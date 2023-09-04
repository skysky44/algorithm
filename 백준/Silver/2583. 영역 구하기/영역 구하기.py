import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
stack = []
count = 0
areas = []

for x in range(N):
    for y in range(M):
        if graph[y][x] == 0:
            stack.append((x, y))
            graph[y][x] = 1
            count += 1
            temp_area = 0
            while stack:
                x, y = stack.pop()
                temp_area += 1
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        stack.append((nx, ny))
            areas.append(temp_area)

# 영역의 개수 출력
print(count)

# 각 영역의 넓이를 오름차순으로 정렬하여 출력
areas.sort()
print(*areas)