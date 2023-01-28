n = int(input())
m = 0
while n >= 0 :
    if n % 5 == 0 :
        m += (n // 5)
        print(m)
        break
    n -= 3
    m += 1
else :
    print(-1)