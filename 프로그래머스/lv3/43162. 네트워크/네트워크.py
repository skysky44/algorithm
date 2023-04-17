from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start, visited, computers):
        visited[start] = True
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
# 여기 생각 안남..
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1

    return answer
