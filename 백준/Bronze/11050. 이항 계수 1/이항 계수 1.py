N, K = map(int, input().split())


def fac(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer


result = (fac(N)//(fac(K)*fac(N-K)))
print(result)
