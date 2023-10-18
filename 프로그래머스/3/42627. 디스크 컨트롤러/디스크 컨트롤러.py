import heapq

def solution(jobs):
    cnt_jobs = len(jobs)
    h = []
    heapq.heapify(h)
    jobs = sorted(jobs)
    time = 0
    answer = 0

    while jobs or h:
        while jobs and jobs[0][0] <= time:
            request_time, duration = jobs.pop(0)
            heapq.heappush(h, (duration, request_time))
        
        if h:
            duration, request_time = heapq.heappop(h)
            time += duration
            answer += (time - request_time)
        else:
            time = jobs[0][0] if jobs else time

    return answer // cnt_jobs


# import heapq

# def solution(jobs):
#     cnt_jobs = len(jobs)
#     h = []
#     heapq.heapify(h)
#     jobs = sorted(jobs)
#     time = 0
#     start = -1
#     answer = 0
#     while jobs:
#         if start < jobs[0][0] <= time:
#             a, b = jobs.pop(0)
#             heapq.heappush(h, (b, a))
            
#         if len(h) > 0:
#             cur = heapq.heappop(h)
#             start = time
#             time += cur[0]
#             answer += time - cur[1]
#         else:
#             time += 1

#     return answer // cnt_jobs


# import heapq

# def solution(jobs):
#     cnt_jobs = len(jobs)
#     h = []
#     heapq.heapify(h)
#     jobs = sorted(jobs)
#     time = 0
#     start = -1
#     answer = 0
#     while jobs:
#         if start < jobs[0][0] <= time:
#             a,b = jobs.pop(0)
#             heapq.heappush(h,(b,a))
            
#         if len(h) > 0:
#             cur = heapq.heappop(h)
#             start = time
#             time += cur[0]
#             answer += time - cur[1]
        
#         else:
#             time += 1


#     return answer // cnt_jobs