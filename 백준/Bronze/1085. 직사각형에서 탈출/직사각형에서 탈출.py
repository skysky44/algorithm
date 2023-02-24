x, y, w, h = map(int, input().split())

distance = min([x-0, w-x, y-0, h-y])

print(distance)
