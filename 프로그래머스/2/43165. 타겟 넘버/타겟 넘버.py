from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0,0)) # 깊이를 표시하기 위해 튜플 사용

    while q:
        temp, idx = q.popleft()
        if idx == len(numbers):    

            if temp == target:
                answer += 1
        else:
            n = numbers[idx]
            q.append((temp + n, idx+1))
            q.append((temp - n, idx+1))
    
    return answer