n = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(n):
    X, Y = map(int, input().split())
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            matrix[x][y] = 1
result = 0
for i in matrix:
    result += sum(i)
print(result)
