score = 0
score_list = []
for _ in range(10):
    score_list.append(int(input()))

for i in score_list:
    before = score
    score += i
    after = score
    check = 100 - score
    if check <= 0:
        break

if abs(100-before) < abs(100-after):
    print(before)
else:
    print(after)