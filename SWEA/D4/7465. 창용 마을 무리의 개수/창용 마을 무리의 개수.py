# import sys
# sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)

    visited = [False]*(N+1)
    visited[0] = True

    while sum(visited) != N+1:
        cnt = 0
        for n in range(1, N+1):
            if visited[n] == False:
                cnt += 1
                start = n
            stack = [start]
            visited[start] = True
            while stack:
                cur = stack.pop()
                for i in matrix[cur]:
                    if not visited[i] == True:
                        visited[i] = True
                        stack.append(i)

    print(f'#{t} {cnt}')
