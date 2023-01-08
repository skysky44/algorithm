import sys
input = sys.stdin.readline
T = int(input())
for c in range(T):
    a, b =map(int, input().split())
    print(f'Case #{c+1}: {a+b} ')