import itertools

h = [int(input()) for _ in range(9)]

for i in itertools.combinations(h, 7):
    if sum(i) == 100:
        result = sorted(i)
        break
print(*result, sep='\n')
