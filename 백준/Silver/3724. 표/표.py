for _ in range(int(input())):
    m, n = map(int, input().split())
    chart = []
    for i in range(n):
        chart.append([*map(int, input().split())])
    result = {}
    for i in range(m):
        t = 1
        for j in range(n):
            t *= chart[j][i]
        result[t] = i+1
    print(result[max(result)])