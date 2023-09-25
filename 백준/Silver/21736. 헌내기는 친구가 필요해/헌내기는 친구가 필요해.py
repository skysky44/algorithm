import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())  # N*M 캠퍼스의 크기
graph = []
for i in range(N):
    temp = list(input().rstrip())
    graph.append(temp)
    if 'I' in temp:  # I 위치를 저장해두기
        j = temp.index('I')
        start = (i, j)  # I 위치


# O는 빈 공간, X는 벽, I는 도연이, P는 사람

# BFS 탐색
q = deque()
q.append(start)
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
cnt = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y + dy[i]
        # 범위 안에 있고 벽이 아니라면
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 'X':
            if graph[nx][ny] == 'P':  # 빈공간이 아니고 사람이면
                cnt += 1
            q.append((nx, ny))
            graph[nx][ny] = 'X'  # 방문한 곳은 벽으로 바꿔주기

if cnt == 0:
    print('TT')
else:
    print(cnt)
