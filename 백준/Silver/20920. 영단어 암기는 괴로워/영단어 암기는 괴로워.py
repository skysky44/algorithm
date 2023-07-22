import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
words = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words[word] += 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in words:
    print(i[0])
