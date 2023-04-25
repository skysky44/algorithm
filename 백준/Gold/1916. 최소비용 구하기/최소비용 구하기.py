# 1916
import heapq  # 우선순위 큐
import sys
input = sys.stdin.readline

N = int(input())  # 노드 수
M = int(input())  # edge 수
graph = [[] for _ in range(N+1)]
# 출발 도시의 번호 / 도착지의 도시 번호 / 버스 비용
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 도착지, 가중치
start, end = map(int, input().split())


def dijkstra(graph, start):
    distances = [int(1e9)]*(N+1)  # 처음 초기값 무한대
    distances[start] = 0  # 시작 노드까지 거리 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # ? 시작 노드부터 탐색 시작

    while queue:
        dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리

        # 기존 거리보다 멀면 패스
        if distances[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노트까지의 거리
            if distance < distances[next_node]:  # 기존 거리 보다 짧으면 갱신
                distances[next_node] = distance
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, next_node])

    return distances


dist_start = dijkstra(graph, start)
print(dist_start[end])  # 도착지점까지의 최단거리
