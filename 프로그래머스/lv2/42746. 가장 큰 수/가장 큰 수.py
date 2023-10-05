def solution(numbers):
    answer = ''
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=lambda x : x*3, reverse=True)

    for number in numbers:
        answer += number
        
    if int(answer) == 0:
        answer = '0'
        
    return answer

# 거의 암기..