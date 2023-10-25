import heapq
def solution(operations):
    queue = []
    # heapq.heapify(queuez)
    for operation in operations:
        cmd, data = operation.split()
        data = int(data)
        if cmd == 'I':
            heapq.heappush(queue, data)
        elif cmd == 'D':
            if queue:
                if data == 1:
                    max_num = max(queue)
                    queue.remove(max_num)
                elif data == -1:
                    heapq.heappop(queue)

    if queue: 
        min_num = heapq.heappop(queue)
        max_num = max(queue)
        answer = [max_num, min_num]
    
    else:
        answer = [0, 0]    
    
    return answer