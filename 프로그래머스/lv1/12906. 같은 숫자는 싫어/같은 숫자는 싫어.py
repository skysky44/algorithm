from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = []
    
    while arr:
        temp = arr.popleft()
        if len(answer) == 0 or answer[-1] != temp:
            answer.append(temp)

    return answer