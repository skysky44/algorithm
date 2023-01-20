s = input()
s_upper = s.upper()
cnt = {}
for i in s_upper:
    cnt[i] = cnt.get(i, 0)+1

sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
if len(sorted_cnt) == 1:
    print(sorted_cnt[0][0])
elif sorted_cnt[0][1] == sorted_cnt[1][1]:
    print('?')
else:
    print(sorted_cnt[0][0])