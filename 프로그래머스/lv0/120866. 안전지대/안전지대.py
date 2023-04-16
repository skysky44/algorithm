def solution(board):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]
    
    # 그래프 전체 순회 하면서 1을 찾기
    
    
    n = len(board)
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for i in range(8):
                    nx, ny = dx[i]+x, dy[i]+y
                    if (0 <= nx < n) and (0 <= ny < n) and  board[nx][ny] != 1:
                        board[nx][ny] = 2
    
    cnt = 0
    for i in board:
        cnt += i.count(0)
    
    answer = cnt
    return answer