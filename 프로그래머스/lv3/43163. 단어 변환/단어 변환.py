from collections import deque
def solution(begin, target, words):
    answer = 0
    
    q = deque([])
    visited = [0]*len(words)
    q.append([begin,0])
    
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            answer = cnt
            break
        else:
            
            for i in range(len(words)):
                if visited[i] == 0:
                    check = 0
                    for j in range(len(begin)):
                        if cur[j] == words[i][j]:
                            pass
                        else:
                            check += 1
                    if check == 1:
                        cnt += 1
                        q.append([words[i], cnt])
                        visited[i] = 1
                           

                
    
    
    return answer