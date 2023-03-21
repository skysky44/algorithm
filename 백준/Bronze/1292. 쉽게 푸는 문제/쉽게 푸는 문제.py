a, b = map(int, input().split())
nums = [0]
result = 0
for i in range(1, b+1):
    for _ in range(i):
        nums.append(i)

for j in range(a, b+1):
    result += nums[j]
print(result)
