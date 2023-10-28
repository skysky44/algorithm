def solution(sizes):
    
    h = []
    w = []
    
    for x, y in sizes:
        if x >= y:
            h.append(x)
            w.append(y)
        else:
            h.append(y)
            w.append(x)
    
    
    answer = max(h)*max(w)

    return answer