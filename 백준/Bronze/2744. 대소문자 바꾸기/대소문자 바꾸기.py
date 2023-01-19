word = input()
new_word = ''
for i in word:
    if i.isupper():
        new_word += i.lower()
    else:
        new_word += i.upper()
print(new_word)
