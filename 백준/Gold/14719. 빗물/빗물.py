import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):  # 첫번째와 마지막은 제외(물이 안고임)
    left = max(block[:i])  # 현재블록 기준 왼쪽 최댓값
    right = max(block[i+1:])  # 현재블록 기준 오른쪽 최댓값
    m = min(left, right)  # 좌우 최댓값 중 작은 값
    if m > block[i]:  # 그 작은 값보다 현재 값이 작다면
        answer += m - block[i]  # 그 차이 만큼 저장

print(answer)
