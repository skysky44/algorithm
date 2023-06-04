a, b = input().split()
a = int(a, 2)
b = int(b, 2)
res = bin(a+b)[2:]
print(res)