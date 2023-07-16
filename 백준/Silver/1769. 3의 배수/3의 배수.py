n = input()
cnt = 0
while int(n)>=10:
    total = 0
    for i in str(n):
        total += int(i)
    n = total
    cnt += 1
print(cnt)
if int(n)%3==0:
    print("YES")
else:   
    print('NO')