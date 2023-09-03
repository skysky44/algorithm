T = int(input())
for i in range(T):
    N = int(input())
    feed = sum(list(map(int, input().split())))
    day = 1
    while N >= feed:
        day += 1
        feed *=4
    print(day)