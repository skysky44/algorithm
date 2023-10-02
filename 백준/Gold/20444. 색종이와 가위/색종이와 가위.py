import sys

input = sys.stdin.readline
n, k = map(int, input().split())

left, right = 0, n // 2 + 1
while left != right:
    mid = (left + right) // 2
    data = (mid + 1) * (n - mid + 1)

    if data == k:
        print("YES")
        sys.exit(0)

    if data > k:
        right = mid

    else:
        left = mid + 1

print("NO")
