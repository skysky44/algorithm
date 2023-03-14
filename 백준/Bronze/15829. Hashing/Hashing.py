L = int(input())
str = input()
h = 0

for i in range(L):
    h += (ord(str[i])-96) * (31 ** i)
print(h % 1234567891)
