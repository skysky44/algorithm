from collections import deque
def solution(priorities, location):
    
    check = deque([0]*len(priorities))
    check[location] = 1
    priorities = deque(priorities)
    answer = 0
    while priorities:
        p = priorities.popleft()
        c = check.popleft()
        if len(priorities) == 0 or p >= max(priorities):
            answer += 1
            if c == 1:
                break
        else:
            priorities.append(p)
            check.append(c)
                
    
    
    
    return answer