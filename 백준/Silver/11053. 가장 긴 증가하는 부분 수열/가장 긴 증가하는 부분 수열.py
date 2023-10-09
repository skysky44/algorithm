import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # N의 범위 만큼 dp 리스트 초기화

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1  # dp[i]를 갱신

print(max(dp))

