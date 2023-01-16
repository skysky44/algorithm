nums = []
absent = []
for _ in range(28):
    num = int(input())
    nums.append(num)

for i in range(1, 31):
    if i not in nums:
        absent.append(i)
absent.sort()
for k in absent:
    print(k)
