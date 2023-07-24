f = [None] * 50
f[1] = f[2] = 1

n = int(input())

def fibonacci(n):
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fibonacci_result = fibonacci(n)
count2 = n - 2

print(fibonacci_result, count2)
