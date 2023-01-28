X = int(input())
n = 0
total = 0
while total < X:
    n += 1
    total = int(n*(n+1)/2)

if n % 2 == 0:
    print(f'{n-total +X}/{total-X+1}')
else:
    print(f'{total-X+1}/{n-total+X}')
