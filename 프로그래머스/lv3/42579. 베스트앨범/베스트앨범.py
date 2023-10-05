# from collections import defalutdict
def solution(genres, plays):
    
    answer = []
    temp = []
    dict_plays = {}
    for i in range((len(genres))):
        if genres[i] in dict_plays:
            dict_plays[genres[i]] += plays[i]
        else:
            dict_plays[genres[i]] = plays[i]
        
        temp.append([genres[i], plays[i], i])
    temp = sorted(temp, key = lambda x : (x[0], -x[1], x[2]))
    # print(temp)
    dict_plays = sorted(dict_plays.items(), key= lambda x : -x[1])
    print(dict_plays)

    for gen in dict_plays:
        cnt = 0
        for i in range(len(temp)):
            if temp[i][0] == gen[0]:
                answer.append(temp[i][2])
                cnt += 1
            if cnt == 2:
                break

                
    return answer

# 장르별 재생 횟수

# 장르 내 재생 횟수 높은 것부터 > 같으면 고유 번호 낮은 것 부터

# 키 : 장르 값:횟수 누적 > 내림차순 정렬

# {classic : [index, 500],[index, 500] }
