while True:
    n = int(input())
    divisor = []
    if n == -1:
        break
    else:
        for i in range(1, n):
            if (n % i) == 0:
                divisor.append(i)

        if sum(divisor) == n:
            print(f'{n} = 1 ', end='')
            for i in divisor[1:]:
                print(f'+ {i} ', end='')
        else:
            print(f'{n} is NOT perfect.', end=' ')
        print()
