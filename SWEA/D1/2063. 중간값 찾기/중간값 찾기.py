T = int(input())

num_list = list(map(int, input().split()))
new_num = sorted(num_list)
print(new_num[T//2])
