import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = {}

for _ in range(N):
    url, ps = input().split()
    list[url] = ps

for _ in range(M):
    print(list[input().rstrip()])