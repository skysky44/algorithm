n, x = map(int, input().split())
list = map(int, input().split())
list2 = []
for i in list:
    if i < x:
        list2.append(i)
print(*list2)