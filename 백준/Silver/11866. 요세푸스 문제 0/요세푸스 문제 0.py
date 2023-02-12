from collections import deque
nums = deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    nums.append(i)
result = []
while nums:
    for _ in range(K-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())
print('<', end='')
print(*result, sep=', ', end='')
print('>')