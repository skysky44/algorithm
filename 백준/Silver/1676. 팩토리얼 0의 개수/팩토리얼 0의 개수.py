N = int(input())

factorial = 1
for i in range(1, N + 1):
    factorial *= i

count = 0

while factorial % 10 == 0:
    count += 1
    factorial //= 10

print(count)
