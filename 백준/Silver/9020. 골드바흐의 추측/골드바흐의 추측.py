T = int(input())


def prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


for _ in range(T):
    n = int(input())
    a = n//2
    b = n//2
    while True:
        if prime_num(a) == True and prime_num(b) == True:
            print(b, a)
            break
        else:
            a += 1
            b -= 1
