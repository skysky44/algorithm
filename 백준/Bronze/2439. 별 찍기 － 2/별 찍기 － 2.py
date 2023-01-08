N = int(input()) 
for n in range(N):
    a='*'*(n+1)
    print (a.rjust(N)) # 오른쪽 정렬

# N = int(input()) 
# for n in range(1, N+1):
#    print(' '*(5-n)+'*'*n)
# 이거 왜 안될까