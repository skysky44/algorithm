n = int(input())
real_score = list(map(int, input().split()))
fake_score = []
m = max(real_score)

for i in real_score:
    fake_score.append(i/m*100)
average = sum(fake_score)/n
print(average)