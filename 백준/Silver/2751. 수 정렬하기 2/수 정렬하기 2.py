import sys
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort(reverse=True)
while len(nums) > 0:
    print(nums.pop())
