import sys
input = sys.stdin.readline
N = int(input())
nums = []
nums_dic = {}
for _ in range(N):
    n = int(input())
    nums.append(n)
    nums_dic[n] = nums_dic.get(n, 0) + 1
print(round(sum(nums)/N))
sorted_nums = sorted(nums)
print(sorted_nums[N//2])
sorted_nums_dic = sorted(
    nums_dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)
if len(sorted_nums_dic) >= 2:
    if sorted_nums_dic[0][1] == sorted_nums_dic[1][1]:
        print(sorted_nums_dic[1][0])
    else:
        print(sorted_nums_dic[0][0])
else:
    print(sorted_nums_dic[0][0])

print(abs(sorted_nums[-1]-sorted_nums[0]))
