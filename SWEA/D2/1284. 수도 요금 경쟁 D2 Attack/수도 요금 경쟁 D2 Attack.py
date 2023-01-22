T = int(input())
for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    a = p*w
    if w <= r:
        b = q
    else:
        b = q + s*(w-r)

    if a <= b:
        result = a
    else:
        result = b

    print(f'#{t} {result}')
