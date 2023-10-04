from collections import Counter
def solution(participant, completion):
    result = list((Counter(participant) - Counter(completion)).keys())
    return result[0]
    
    

    # dictionary로 풀거나 Counter 사용하기
    