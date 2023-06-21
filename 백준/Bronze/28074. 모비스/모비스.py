aphabet = ['M', 'O', 'B', 'I', 'S']
word = input()
result = True

for i in aphabet :
    if i not in word :
        result = False
        break

if result :
    print('YES')
else :
    print('NO')