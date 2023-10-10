import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # N의 범위 만큼 dp 리스트 초기화

for i in range(N):
    max_dp = 1
    for j in range(i):
        if A[j] < A[i] and max_dp < dp[j] + 1:
            max_dp = dp[j] + 1
    dp[i] = max_dp

print(max(dp))
