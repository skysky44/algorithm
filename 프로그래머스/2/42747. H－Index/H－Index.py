def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for i, citation in enumerate(citations):
        if i >= citation:  # h번 이상 인용된 논문이 h편 이상일 때
            return i
    
    return len(citations)

# def solution(citations):
#     citations = sorted(citations, key = lambda x : -x)
#     max_h = 1
    
#     for citation in citations:
#         cnt = 0
#         for c in citations:
#             if citation <= c:
#                 cnt += 1
#                 if cnt == check:
#                     break
#         if max_h <= cnt:
#             max_h = cnt    
#     answer = max_h
#     return answer