n = int(input())
for _ in range(n):
    score = 0
    result = 0
    str = input()
    for i in str:
        if i == 'O':
            result += 1 + score
            score += 1
        else:
            score = 0
    print(result)