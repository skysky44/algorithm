T = int(input())
for t in range(1, T+1):
    h, w, n = map(int, input().split())
    floor = n % h
    number = n//h
    if floor == 0:
        floor += h
        number -= 1
    else:
        pass
    room = floor*100+number+1
    print(room)
