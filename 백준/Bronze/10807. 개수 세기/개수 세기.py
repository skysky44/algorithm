n = int(input())
n_list = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in n_list:
    if i == v:
        cnt += 1
print(cnt)
