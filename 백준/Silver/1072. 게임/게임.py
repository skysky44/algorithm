X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    a = 0
    l = 1
    r = X

    while l <= r:
        m = (l + r) // 2
        if (Y + m) * 100 // (X + m) <= Z:
            l = m + 1
        else:
            a = m
            r = m - 1

    print(a)
