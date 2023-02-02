N = input()
num = []
for i in N:
    num.append(i)
new_num = sorted(num, reverse=True)
for i in new_num:
    print(i, end='')
