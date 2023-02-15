doc = input()
word = input()
cnt = 0
n = 0
while n <= len(doc) - len(word):
    if doc[n:n + len(word)] == word:
        cnt += 1
        n += len(word)
    else:
        n += 1
print(cnt)
