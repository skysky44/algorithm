import sys
input = sys.stdin.readline
N = int(input())
books = {}
for i in range(N):
    title = str(input().rstrip())
    books[title] = books.get(title, 0) + 1

max_num = max(books.values())
result = []
for title in books:
    if books[title] == max_num:
        result.append(title)
result.sort()
print(result[0])
