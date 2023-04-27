import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V + 1)]
distance = [INF]*(V+1)


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가기 위한 거리 w


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        current_destination, current_distance = heapq.heappop(queue)
        for i in graph[current_distance]:
            cost = current_destination + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
