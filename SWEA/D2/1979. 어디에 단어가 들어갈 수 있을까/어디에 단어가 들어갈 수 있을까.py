T = int(input())
for t in range(1, 1+T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    check = 0  # 누적칸 , 단어 들어갈 자리수 cnt
    count = 0
    for x in range(N):  # 칸 돌면서 확인
        for y in range(N):
            # 1. 첫째칸이면 누적 칸 초기화/ 아니면 진행
            # 2. 마지막 칸이거나 0 이 나오면 누적칸이 3인지 확인후 3이면 단어자리수 더하기 1 하고 초기화 / 누적칸 3아니면  그냥 누적칸 초기화
            if matrix[x][y] == 1:
                check += 1
                if y == N-1:
                    if check == K:
                        count += 1
                        check = 0
                    elif check != K:
                        check = 0
            elif matrix[x][y] == 0:
                if check == K:
                    count += 1
                    check = 0
                elif check != K:
                    check = 0
    for x in range(N):
        for y in range(N):
            if matrix[y][x] == 1:
                check += 1
                if y == N-1:
                    if check == K:
                        count += 1
                        check = 0
                    elif check != K:
                        check = 0
            elif matrix[y][x] == 0:
                if check == K:
                    count += 1
                    check = 0
                elif check != K:
                    check = 0

    print(f'#{t} {count}')
