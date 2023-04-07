from collections import deque

n = int(input())
base_graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    base_graph.append(temp)

max_height = max(map(max, base_graph))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_safe_zone_cnt = 1  # 아무 지역도 물에 잠기지 않을 경우를 대비해 1로 초기화

for water_height in range(1, max_height+1):  # 물 높이를 1부터 최대 높이까지 변경
    graph = base_graph
    # base_graph를 복사하여 graph 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= water_height:
                graph[i][j] = 0  # 물에 잠긴 구역을 0으로 변경

    visited = [[False]*n for _ in range(n)]  # 방문 여부를 체크할 리스트
    safe_zone_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > 0:
                safe_zone_cnt += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
    max_safe_zone_cnt = max(max_safe_zone_cnt, safe_zone_cnt)

print(max_safe_zone_cnt)