a, b = map(str, input().split())

a_mat = [int(i) for i in a]
b_mat = [int(j) for j in b]
print(sum(a_mat)*sum(b_mat))
