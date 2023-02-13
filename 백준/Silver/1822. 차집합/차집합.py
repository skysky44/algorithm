n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(a-b) == 0:
    print(0)
else:
    print(len(a-b))
    result = sorted(a-b)
    print(*result)
