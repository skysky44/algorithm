n = int(input())
cnt = 0

if n < 100:
    cnt = n
else:
    cnt = 99
    for i in range(100, n+1):
        i = str(i)
        if int(i[1]) - int(i[0]) == int(i[2]) - int(i[1]):
            cnt += 1
print(cnt)