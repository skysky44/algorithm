import heapq
def solution(scoville, K):
    
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        cnt += 1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
    
    return  cnt  