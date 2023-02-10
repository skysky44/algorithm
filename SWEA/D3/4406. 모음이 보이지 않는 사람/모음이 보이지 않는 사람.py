T = int(input())
for t in range(1, T + 1):
    word = input()
    for i in ['a', 'e', 'i', 'o', 'u']:
        word = word.replace(i, '')
    print(f'#{t} {word}')
