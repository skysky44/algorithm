N = str(input())
nums = [0] * 10
for i in str(N):
    if i == "9" or i == "6":
        if nums[6] == nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[int(i)] += 1

print(max(nums))