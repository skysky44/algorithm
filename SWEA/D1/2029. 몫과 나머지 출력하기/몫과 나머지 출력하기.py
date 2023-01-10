T = int(input())
for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    quotient = a // b
    remainder = a % b
    print(f'#{t} {quotient} {remainder}')
