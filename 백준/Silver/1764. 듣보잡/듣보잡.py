N, M = map(int, input().split())
l = set()
s = set()
for _ in range(N):
    l.add(input())
for _ in range(M):
    s.add(input())
ls = sorted(l & s)
print(len(ls))
print(*ls, sep='\n')
