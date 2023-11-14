from collections import deque


def check(input, person):
    temp = person.popleft()
    if input == temp:
        point =  1
    else:
        point =  0
    person.append(temp)
    
    return point


def solution(answers):
    person_1 = deque([1, 2, 3, 4, 5])
    person_2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    person_3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    points = {
        1 : 0,
        2 : 0,
        3 : 0
    }
    
    for answer in answers:
        points[1] += check(answer, person_1)
        points[2] += check(answer, person_2)
        points[3] += check(answer, person_3)

    points = sorted(points.items(), key = lambda x : x[1], reverse=True)


    result = []
    for point in points:
        if result:
            if point[1] == points[0][1]:
                result.append(point[0])
            else:
                break
        else:
            result.append(point[0])

    return result
