import sys
input = sys.stdin.readline
N = int(input())
files = []
for _ in range(N):
    file = input().strip()
    files.append(file)

extension = {}
for file in files:
    ext = file[file.index('.')+1:]
    extension[ext] = extension.get(ext, 0) + 1
result = sorted(extension.items(), key=lambda x: x[0])

for i in result:
    print(*i)