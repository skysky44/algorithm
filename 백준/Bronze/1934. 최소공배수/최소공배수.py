T = int(input())

# 최대 공약수


def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    result = x
    return result

# 최소 공배수


def lcm(x, y):
    result = (x*y)//gcd(x, y)
    return result


for t in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))

