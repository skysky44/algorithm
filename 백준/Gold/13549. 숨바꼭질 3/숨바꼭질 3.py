from collections import deque
N, K = map(int, input().split())

visited = [-1]*100001

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        
        cur = q.popleft()

        if cur == K:
            print(visited[cur])
            return
        
        next = [2*cur, cur-1, cur+1]

        for i in next:
            if 0 <= i < 100001 and visited[i] == -1:

                if i == 2*cur:
                    visited[i] =  visited[cur]
                    q.appendleft(i)
                else:
                    visited[i] = visited[cur] + 1
                    q.append(i)
bfs(N)