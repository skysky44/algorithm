import sys
input = sys.stdin.readline
N = int(input())
cards = set(map(int, input().split()))

M = int(input())
checks = list(map(int, input().split()))
for check in checks:
    if check in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
