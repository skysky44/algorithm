num_list = list(map(int, input().split()))

min_num = min(num_list)
cnt = 0
while True:
    cnt = 0
    for i in range(len(num_list)):
        if min_num % num_list[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(min_num)
        break
    min_num += 1
