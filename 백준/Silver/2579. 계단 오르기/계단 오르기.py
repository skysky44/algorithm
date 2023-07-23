import sys
input = sys.stdin.readline
N = int(input())
stair = [int(input()) for i in range(N)]
dp = [0]*(N)
if len(stair) <= 2:
    print(sum(stair))
else:  # 계단이 3개 이상일 때
    dp[0] = stair[0]  # 첫째 계단
    dp[1] = stair[0]+stair[1]  # 둘째 계단까지
    for i in range(2, N):  # 3번째 계단 부터 dp 최대값 구하기
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])