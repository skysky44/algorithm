T = 10
for t in range(1, T + 1):
    dump = int(input())
    height = list(map(int, input().split()))
    for _ in range(dump):
        height[height.index(max(height))] = max(height)-1
        height[height.index(min(height))] = min(height)+1
    print(f'#{t} {max(height)-min(height)}')