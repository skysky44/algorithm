import sys
input = sys.stdin.readline

def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())
ban = round2(n*0.15)

if n == 0:
    print(0)
else:
    score = []
    for _ in range(n):
        score.append(int(input()))
    score.sort()
    

    res = 0
    for i in range(ban, n-ban):
        res += score[i]
    res = res/(n-2*ban)
    print(round2(res))