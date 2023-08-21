import sys
input = sys.stdin.readline

n, han, jimin = map(int, input().split())
rounds = 0

while han != jimin:
    han = (han + 1) // 2
    jimin = (jimin + 1) // 2
    rounds += 1

print(rounds)
