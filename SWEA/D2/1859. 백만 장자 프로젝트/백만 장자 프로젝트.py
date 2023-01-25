T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0
    max_price = nums[-1]
    for n in range(N-1, -1, -1):
        if nums[n] >= max_price:
            max_price = nums[n]
        result += max_price - nums[n]
    print(f'#{t} {result}')
