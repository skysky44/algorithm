import sys
input = sys.stdin.readline
N, M = map(int, input().split())
basket = {}
for n in range(1, N+1):
    basket[n] = n

for _ in range(M):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

for values in basket.values():
    print(values, end=' ')
