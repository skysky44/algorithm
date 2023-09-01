import sys
input = sys.stdin.readline
a,b = map(int, input().split())

case = int(input())
arr=[]
for i in range(case):
    arr.append(int(input()))

sum1 = abs(b-a)

for i in range(case):
    arr[i] = abs(b-arr[i])

sum2=min(arr)

print(min(sum1,sum2+1))