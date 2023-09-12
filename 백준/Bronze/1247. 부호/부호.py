import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    nums = [int(input()) for i in range(N)]
    if sum(nums) == 0:
        print("0")
    elif sum(nums) > 0:
        print("+")
    else:
        print("-")
