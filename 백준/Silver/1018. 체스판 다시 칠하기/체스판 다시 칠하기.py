N, M = map(int, input().split())
board = [input() for _ in range(N)]
min_cnt = N*M
for color in ['W', 'B']:  # 첫째 칸 색
    for x in range(N-8+1):
        for y in range(M-8+1):
            cnt = 0
            for i in range(x, x+8):
                for j in range(y, y+8):
                    if (i + j) % 2 == 0:
                        if board[i][j] == color:
                            pass
                        elif board[i][j] != color:
                            cnt += 1
                    elif (i + j) % 2 != 0:
                        if board[i][j] != color:
                            pass
                        elif board[i][j] == color:
                            cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt
print(min_cnt)
