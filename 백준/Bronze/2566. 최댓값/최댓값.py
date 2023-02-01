import sys
input = sys.stdin.readline
matrix = []
for _ in range(9):
    nums = list(map(int, input().split()))
    matrix.append(nums)

max_value = 0
location = [0, 0]

for x in range(9):
    for y in range(9):
        if matrix[x][y] > max_value:
            max_value = matrix[x][y]
            location[0] = x
            location[1] = y
print(max_value)
print(location[0]+1, location[1]+1)