S = input()
result = set()
for i in range(0, len(S)+1):
    for j in range(i+1, len(S)+1):
        result.add(S[i:j])

print(len(result))
