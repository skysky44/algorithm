nums = []
for _ in range(10):
    nums.append(int(input()) % 42)

remainder = set(nums)
print(len(remainder))