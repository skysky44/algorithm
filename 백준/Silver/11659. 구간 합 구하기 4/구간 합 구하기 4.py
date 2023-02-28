import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]*(N+1)
for t in range(N):
    sums[t+1] = sums[t]+nums[t]

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j]-sums[i-1])
