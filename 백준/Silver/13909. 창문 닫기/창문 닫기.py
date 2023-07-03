import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
x = 1
while x*x <= N:
    x += 1
    cnt += 1
print(cnt)
