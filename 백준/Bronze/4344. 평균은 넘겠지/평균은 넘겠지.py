c = int(input())
for _ in range(c):
    score_list = list(map(int, input().split()))
    average = (sum(score_list)-score_list[0])/score_list[0]
    cnt = 0
    for i in range(1, score_list[0]+1):
        if score_list[i] > average:
            cnt += 1
    result = (cnt/score_list[0])*100
    print(f'{result:.3f}%')