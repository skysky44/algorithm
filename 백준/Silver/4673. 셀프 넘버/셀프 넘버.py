자연수 = set(range(1, 10001))
생성자수 = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    생성자수.add(i)

셀프넘버 = sorted(자연수 - 생성자수)
for i in 셀프넘버:
    print(i)