import sys
input = sys.stdin.readline
N, M = map(int, input().split())
strings = []
for _ in range(N):
    strings.append(input().strip())
cnt = 0
for _ in range(M):
    check = input().strip()
    if check in strings:
        cnt += 1
print(cnt)