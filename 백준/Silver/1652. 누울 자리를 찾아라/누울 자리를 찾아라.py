
N = int(input())
room = []
for _ in range(N):
    s = list(input())
    room.append(s)

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            cnt1 += 1
            if cnt1 == 2:
                cnt2 += 1
        elif room[i][j] == 'X':
            cnt1 = 0
    else:
        cnt1 = 0

cnt3 = 0
cnt4 = 0
for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            cnt3 += 1
            if cnt3 == 2:
                cnt4 += 1
        elif room[j][i] == 'X':
            cnt3 = 0
    else:
        cnt3 = 0
print(cnt2, cnt4)