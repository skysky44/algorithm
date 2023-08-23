import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
result = defaultdict(int)
for _ in range(n):
    name = str(input().strip())
    k, m = map(int, input().split())
    cnt = 0
    while k <= m:
        m = m-k+2
        cnt += 1
    result[name] = cnt

print(sum(result.values()))
result = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(result[0][0])