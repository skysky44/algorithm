# 투명
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            graph[x][y] += 1

cnt = 0
for x in range(100):
    for y in range(100):
        if graph[x][y] > M:
            cnt += 1

print(cnt)

