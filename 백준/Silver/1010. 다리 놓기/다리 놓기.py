T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a = 1
    b = 1
    c = 1

    for i in range(1, M+1):
        a *= i
    for j in range(1, M-N+1):
        b *= j
    for k in range(1, N+1):
        c *= k

    print(int(a/(b*c)))
