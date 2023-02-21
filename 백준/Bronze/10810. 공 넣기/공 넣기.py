import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bascket = {}
for n in range(N):
    bascket[n] = 0

for _ in range(M):
    i, j, k = map(int, input().split())
    for number in range(i-1, j):
        bascket[number] = k

for values in bascket.values():
    print(values)