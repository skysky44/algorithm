import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

num_list.sort()
for target in target_list:
    start = 0
    end = len(num_list)-1
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        if num_list[mid] == target:
            cnt += 1
            break
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print(cnt)
