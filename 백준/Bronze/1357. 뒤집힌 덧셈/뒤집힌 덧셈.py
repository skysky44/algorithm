X, Y = map(int, input().split())


def Rev(x):
    x = str(x)
    return int(x[::-1])


print(Rev(Rev(X)+Rev(Y)))
