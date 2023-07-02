n = int(input())

start, serve, end = 1, 2, 3


def hanoi(n, start, end, serve):
    if n == 1:  # 한 개 일 때 시작 기둥에서 끝 기둥으로
        print(start, end)
        return

    else:
        hanoi(n-1, start, serve, end)
        print(start, end)
        hanoi(n-1, serve, end, start)


print(2**n-1)  # K를 하나씩 더하는 방법은?
hanoi(n, start, end, serve)
