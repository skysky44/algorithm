import sys
input = sys.stdin.readline
N, K = map(int, input().split())
temps = list(map(int, input().split()))

sums = [0]*(N-K+1)

for i in range(K):
    sums[0] += temps[i]

for j in range(N-K):
    sums[j+1] = sums[j]-temps[j]+temps[j+K]
print(max(sums))
