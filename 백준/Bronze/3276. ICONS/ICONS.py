n = int(input())
row = 0
col = 0

while True:
    if row * col >= n:
        break
    row += 1

    if row * col >= n:
        break
    col += 1
print(row, col)