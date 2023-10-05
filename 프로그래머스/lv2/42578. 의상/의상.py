from collections import defaultdict

def solution(clothes):
    dic_cloth = defaultdict(int)
    for cloth in clothes:
        dic_cloth[cloth[1]] += 1
        
    answer = 1
    if dic_cloth:
        for i in dic_cloth.values():
            answer *= i+1
        answer -= 1
    else:
        answer = 0

    return answer
# def solution(clothes):
#     dic_cloth = {}
#     for cloth in clothes:
#         if cloth[1] in dic_cloth:
#             dic_cloth[cloth[1]] += 1
#         else:
#             dic_cloth[cloth[1]] = 1
    
#     answer = 1
#     if dic_cloth:
#         for i in dic_cloth.values():
#             answer *= i+1
#         answer -= 1
#     else:
#         answer = 0

#     return answer