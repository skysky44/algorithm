# N-Queen
n = int(input())
answer = 0
row = [0]*n

# 해당 위치에 퀸을 놓을 수 있는지 없는지 판단 함수

# 퀸을 놓지 못하는 경우
# 1. 같은 열에 다른 퀸이 있는 경우: row[x] == row[i]
# 2. 왼쪽 대각선, 오른쪽 대각선에 달느 퀸이 있는 경우: abs(row[x] - row[i]) == abs(x - i)


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

# 퀸 배치 함수: [x, i]에 퀸 놓기


def n_queens(x):
    global answer
    if x == n:  # 끝 행까지 가면 answer 추가
        answer += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):  # 놓을 수 있으면 진행
                n_queens(x+1)


n_queens(0)
print(answer)
