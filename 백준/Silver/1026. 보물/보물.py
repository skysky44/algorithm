import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list, reverse=False)

result = 0

for i in range(n):
    result += sorted_a[i]*sorted_b[i]

print(result)
