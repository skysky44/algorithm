import sys
import pprint
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    # m*n
    grid = []
    for _ in range(m):
        grid.append(input().split())

    # pprint.pprint(grid)
    cnt = 0
    cnt2 = 0
    while True:
        cnt = 0
        for i in range(n):
            for j in range(m-1):
                # print(j, i, 0)

                if grid[j][i] == '1' and grid[j+1][i] == '0':
                    grid[j][i] = '0'
                    grid[j+1][i] = '1'
                    cnt += 1
        cnt2 += cnt
        if cnt == 0:
            break

    # pprint.pprint(grid)
    print(cnt2)
