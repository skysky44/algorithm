T = int(input())
for t in range(1, T + 1):
    nums = str(input())
    y = nums[0:4]
    m = nums[4:6]
    d = nums[6:8]
    if int(m) == 2:
        if 1 <= int(d) <= 28:
            print(f'#{t} {y}/{m}/{d}')
        else:
            print(f'#{t} -1')
    elif int(m) in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= int(d) <= 31:
            print(f'#{t} {y}/{m}/{d}')
        else:
            print(f'#{t} -1')
    elif int(m) in [4, 5, 9, 11]:
        if 1 <= int(d) <= 30:
            print(f'#{t} {y}/{m}/{d}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')
