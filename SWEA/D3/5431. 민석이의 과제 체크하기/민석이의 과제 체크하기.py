# import sys
# sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    students = list(map(int, input().split()))
    print(f'#{t}', end=' ')
    for i in range(1, N+1):
        if i in students:
            pass
        else:
            print(i, end=' ')
    print()
