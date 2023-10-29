import heapq
import sys
input = sys.stdin.readline

N = int(input())

lec_info = []
for i in range(N):
    temp = list(map(int, input().split()))
    lec_info.append(temp)

lec_info = sorted(lec_info, key=lambda x: x[1])  # 시작시간 오름차순 정렬

end_heap = []
count = 0

for i in lec_info:
    # 끝나는 시간 중 최솟값(먼저 끝나는)보다 시작시간이 크거나 같으면
    while end_heap and end_heap[0] <= i[1]:
        heapq.heappop(end_heap)  # heap에서 가장 작은 원소 내보냄
    heapq.heappush(end_heap, i[2])  # 그 i의 끝나는 시간 힙에 추가
    # 시작 시간이 끝나는 시간보다 빨라서 강의실 배정을 못한 강의가 heap에 남음
    count = max(count, len(end_heap))

print(count)
