word = list(input())
result = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        x, y, z = word[:i][::-1], word[i:j][::-1], word[j:][::-1]
        result.append(''.join(x+y+z))
print(sorted(result)[0])