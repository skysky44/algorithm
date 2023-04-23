N, B = input().split()
# B진법
# B진법 수를 10진법으로 바꾸면...
# 36진법 ZZZZZ
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
answer = 0
for i in range(len(N)-1,-1,-1):
    answer += number.index(N[i])*(int(B)**i)

print(answer)
