T = int(input())
results = []

for _ in range(T):
    _, N = input(), int(input())
    candy_list = [int(input()) for _ in range(N)]

    if sum(candy_list) % N == 0:
        results.append('YES')
    else:
        results.append('NO')

for result in results:
    print(result)