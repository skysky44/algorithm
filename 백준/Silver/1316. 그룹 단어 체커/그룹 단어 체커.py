N = int(input())
group = []
for _ in range(N):
    word = input()
    alphabet = []
    check = ''

    for i in word:
        if check != i and i in alphabet:
            break
        elif check != i and i not in alphabet:
            check = i
            alphabet.append(check)

    else:
        group.append(word)
print(len(group))
