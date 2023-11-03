import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tem = list(map(int, input().split()))
result = []
result.append(sum(tem[:K]))

for i in range(N-K):
    result.append(result[i] - tem[i] + tem[i+K])

print(max(result))
