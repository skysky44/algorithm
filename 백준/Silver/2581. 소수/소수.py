M = int(input())
N = int(input())
prime_number = []
for num in range(M, N+1):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        prime_number.append(num)
if prime_number:
    print(sum(prime_number), min(prime_number), sep='\n')
else:
    print(-1)