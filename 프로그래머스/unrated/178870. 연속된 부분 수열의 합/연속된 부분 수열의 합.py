def solution(sequence, k):
    start = 0
    end = 0
    current_sum = 0
    result = []
    
    while start < len(sequence):
        if current_sum < k:
            if end == len(sequence):
                break
            current_sum += sequence[end]
            end += 1
        
        elif current_sum >= k:
            if current_sum == k:
                if not result or (end - start - 1) < (result[1] - result[0]):
                    result = [start, end - 1]
            current_sum -= sequence[start]
            start += 1

    return result

