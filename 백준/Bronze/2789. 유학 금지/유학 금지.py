word = input()
new_word = ''
for i in word:
    if i not in 'CAMBRIDGE':
        new_word += i
print(new_word)