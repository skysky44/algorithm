N = int(input())
time = sum([*map(int, input().split())]) + (N - 1) * 8
print(time // 24, time % 24)