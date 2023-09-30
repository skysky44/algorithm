N, K = map(int, input().split())
nums = list(map(int, input().split(',')))
for _ in range(K):
    t = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
    nums = t
print(*nums, sep=',')