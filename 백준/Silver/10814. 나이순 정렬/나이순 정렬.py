n = int(input())
members = [list(input().split()) for _ in range(n)]
result = sorted(members, key=lambda x: int(x[0]))  # 입력이 str이라서 변환
for i in result:
    print(*i)