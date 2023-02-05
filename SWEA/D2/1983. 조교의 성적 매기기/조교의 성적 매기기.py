# import sys
# sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    s = []
    a = []
    student = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for _ in range(N):
        s.append(list(map(int, input().split())))
    for i in range(N):
        a.append((s[i][0]*0.35)+(s[i][1]*0.45)+(s[i][2]*0.20))
    b = sorted(a, reverse=True)
    c = b.index(a[K-1])

    for i in grade:
        for j in range(N//10):
            student.append(i)
    print(f'#{t} {student[c]}')
