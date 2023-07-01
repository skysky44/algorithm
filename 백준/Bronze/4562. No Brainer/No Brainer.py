t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if n < m:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")