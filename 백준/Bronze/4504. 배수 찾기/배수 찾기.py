n = int(input())

while True:
    a = int(input())
    if a == 0:
        break
    if a % n == 0:
        print(a, " is a multiple of ", n, ".", sep="")
    else:
        print(a, " is NOT a multiple of ", n, ".", sep="")