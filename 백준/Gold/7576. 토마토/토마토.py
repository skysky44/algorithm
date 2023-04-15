from collections import deque

M, N = map(int, input().split())

# M 상자 가로 /// N 상자 세로
# 1 익은 토마토 , 0 익지 않은 토마토, -1 토마토 안들어있음
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

queue = deque([])  # 큐를 초기화

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토의 위치를 큐에 추가
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            queue.append((x, y, 0))  # 익은 토마토의 위치와 일수(0)를 함께 큐에 추가

# BFS 수행
max_depth = 0  # 최대 일수를 저장할 변수
while queue:
    x, y, depth = queue.popleft()
    max_depth = depth  # 현재 일수를 최대 일수로 업데이트

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = 1  # 익지 않은 토마토를 익은 토마토로 변경
            queue.append((nx, ny, depth + 1))  # 다음 위치와 일수(현재 일수 + 1)를 함께 큐에 추가

# 모든 토마토가 익지 않은 경우에는 -1 출력, 그 외에는 최대 일수 출력
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit()

print(max_depth)
