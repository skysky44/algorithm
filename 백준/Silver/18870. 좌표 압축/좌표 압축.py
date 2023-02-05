N = int(input())
nums = list(map(int, input().split()))
new_nums = sorted(list(set(nums)))
dict_nums = {new_nums[i]: i for i in range(len(new_nums))}

for i in nums:
    print(dict_nums[i], end=' ')

# .index 사용하면 시간복잡도 O(n) 이라서.. 시간초과
