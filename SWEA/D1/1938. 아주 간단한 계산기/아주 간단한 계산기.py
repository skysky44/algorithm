a, b = map(int, input().split())
calculation = [a+b, a-b, a*b, a//b]
for result in calculation:
    print(result)