for _ in range(int(input())):
    a, b = input().split()
    a, b = int(a[::-1]), int(b[::-1])
    result = int(str(a+b)[::-1])
    print(result)