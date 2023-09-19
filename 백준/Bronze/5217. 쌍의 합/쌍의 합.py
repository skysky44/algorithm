import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    first = 1
    print(f"Pairs for {n}:", end=' ')

    for k in range((n - 1) // 2):
        if k != 0:
            print(',', end=' ')
        print(first, n - first, end='')
        first += 1

    print()