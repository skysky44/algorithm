def solution(s):
    numbers = list(map(int, s.split()))
    min_num = min(numbers)
    max_num = max(numbers)
    answer = f"{min_num} {max_num}"
    return answer
