N = int(input())
word = list(input())

for _ in range(N-1):
    word2 = input()
    for n in range(len(word)):
        if word[n] == word2[n]:
            continue
        else:
            word[n] = "?"
print(*word, sep = "")