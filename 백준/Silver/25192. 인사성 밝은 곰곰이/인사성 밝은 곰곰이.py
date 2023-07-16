import sys
input = sys.stdin.readline

N = int(input())
cnt_list = set()
cnt = 0

for _ in range(N):
    word = input().rstrip()  # 개행 문자 제거
    if word == 'ENTER':
        cnt_list.clear()
    else:
        if word not in cnt_list:
            cnt += 1
            cnt_list.add(word)

print(cnt)
