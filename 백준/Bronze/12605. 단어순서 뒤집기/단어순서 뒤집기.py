N = int(input())

for n in range(1, N+1):
    words = input().split()
    result = []
    for _ in range(len(words)):
        for i in words.pop():
            result.append(i)
        result.append(' ')
    print(f'Case #{n}:', end=' ')
    for i in result:
        print(i, end='')
