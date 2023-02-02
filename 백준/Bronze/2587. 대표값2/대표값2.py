nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)
nums.sort()
average = sum(nums)//5
median = nums[2]
print(average)
print(median)
