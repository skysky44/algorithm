score = []
for i in range(1,9):
    score.append((int(input()),i))
score.sort(reverse = True)

total = 0
rank = []
for score,n in score[:5]:
    total+= score
    rank.append(n)
print(total)
print(*sorted(rank))