def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer