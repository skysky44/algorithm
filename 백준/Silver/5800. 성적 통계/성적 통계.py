k = int(input())

class_num = 1
for _ in range(k):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    score = sorted(arr[1::], reverse=True)

    max_v = max(score) 
    min_v = min(score)
    gap_v = score[0] - score[1]
    for i in range(2, len(score)):
        gap_v = max(gap_v, score[i - 1] - score[i])

    print('Class', class_num)
    print('Max', max_v, end=", ")
    print('Min', min_v, end=", ")
    print('Largest gap', gap_v)
    class_num += 1