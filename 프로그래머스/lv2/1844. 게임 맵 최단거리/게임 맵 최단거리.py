from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    # n행 m열
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    graph = maps
    stack = deque([])
    stack.append((0, 0))
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 생각..
                stack.append((nx, ny))
    
    # 모름
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1] 
        
    return answer