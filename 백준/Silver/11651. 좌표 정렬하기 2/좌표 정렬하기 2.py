import sys
input = sys.stdin.readline
N = int(input())
list_xy = []
for _ in range(N):
    xy = list(map(int, input().split()))
    list_xy.append(xy)

sorted_xy = sorted(list_xy, key=lambda x: (x[1], x[0]))
for i in sorted_xy:
    print(*i)
