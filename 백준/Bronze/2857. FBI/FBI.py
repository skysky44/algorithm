flag = 0
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        flag = 1
        print(i, end=' ')
if flag == 0:
    print('HE GOT AWAY!')
