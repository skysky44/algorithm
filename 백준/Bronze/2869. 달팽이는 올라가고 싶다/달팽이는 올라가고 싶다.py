a, b, v = map(int, input().split())

d = (v-a) // (a-b)
if (v-a) % (a-b) == 0:
    print(d+1)
else:
    print(d+2)
