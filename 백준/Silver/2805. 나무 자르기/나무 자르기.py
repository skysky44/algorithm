import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
while start <= end:
    mid = (start+end)//2
    cut_sum = 0
    for j in trees:
        if j-mid >= 0:
            cut_sum += (j-mid)
    if cut_sum >= M:
        start = mid+1
    else:
        end = mid-1
print(end)
