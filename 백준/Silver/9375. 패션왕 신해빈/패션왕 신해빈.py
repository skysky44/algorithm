T = int(input())
for _ in range(T):
    cloth = {}
    n = int(input())
    for _ in range(n):
        item, category = map(str, input().split())
        cloth[category] = cloth.get(category, 1) + 1
    result = 1
    for value in cloth.values():
        result *= value
    print(result-1)
