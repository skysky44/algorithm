import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
# space = [list(map(int, input().split())) for _ in range(n)]
space = []
for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        j = temp.index(9)
        start = (i, j)
    space.append(temp)


# start
# 너비우선 탐색 상하 좌우 확인 > 클, 같, 작
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # 가장 위 > 가장 왼쪽 순
size = 2


def bfs(start, space, size):
    q = deque()
    q.append(start)

    distance = [[0] * n for _ in range(n)]  # 최단 거리
    visited = [[0] * n for _ in range(n)]
    targets = []
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if space[nx][ny] <= size:  # 사이즈 같을 때는 안먹지만 지나가니까 거리가 필요
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1

                    if 0 < space[nx][ny] < size:
                        targets.append((nx, ny, distance[nx][ny]))

    # ㅠㅠ 거리>
    return sorted(targets, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0  # 상어가 먹은 물고기의 수(자신의 크기만큼 먹으면 커짐)
time = 0
while True:
    shark = bfs(start, space, size)
    # 먹을 수 있는 물고기 있는지 파악
    if len(shark) == 0:  # 완전탐색 할 뻔
        break

    # 정렬된 결과를 반영해주면서 먹을 물고기 선택
    nx, ny, dist = shark.pop()

    # 움직인 칸의 수는 시간
    time += dist
    space[start[0]][start[1]], space[nx][ny] = 0, 0  # 기존 상어자리와 먹은 물고기 위치 업데이트
    start = (nx, ny)  # 상어가 옮겨간 위치(상어의 좌표를 먹은 물고기의 좌표 수정 후 다음 턴)
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(time)
