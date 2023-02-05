# import sys
# sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    total = []
    for x in range(N-M+1):
        for y in range(N-M+1):
            fly = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    fly += matrix[i][j]
            total.append(fly)

    print(f'#{t} {max(total)}')
