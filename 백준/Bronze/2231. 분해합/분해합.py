N = int(input())

for i in range(1, N+1):
    N_sum = 0
    for j in str(i):
        N_sum += int(j)
    if N == i + N_sum:
        print(i)
        break
else:
    print(0)
