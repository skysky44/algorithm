a, b = map(str, input().split())
c, d = int(a[::-1]), int(b[::-1])
if c > d:
    print(c)
else:
    print(d)