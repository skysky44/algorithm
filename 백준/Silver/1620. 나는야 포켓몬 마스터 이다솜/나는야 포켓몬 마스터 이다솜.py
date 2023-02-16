import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    pokemon[str(i)] = input().strip()
# 딕셔너리 키, 값 바꿔서 저장
numbers = {value: key for key, value in pokemon.items()}
for _ in range(M):
    inp = input().strip()
    result = pokemon.get(inp, 0)
    if result == 0:
        result = numbers.get(inp)
    print(result)
