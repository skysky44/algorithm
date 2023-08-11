message = input().strip()

length = len(message)
r, c = 0, 0


for i in range(1, length):
    if length % i == 0 and i <= length // i:
        r = i
        c = length // i

result = [[""] * c for _ in range(r)]
idx = 0
for j in range(c):
    for i in range(r):
        result[i][j] = message[idx]
        idx += 1

decoded_message = "".join(["".join(row) for row in result])
print(decoded_message)
