T = int(input())
for _ in range(T) :
    input()
    N, M = map(int, input().split())
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    sj = sorted(sj, reverse=True)
    sb = sorted(sb, reverse=True)

    while sj and sb:
        if sj[-1] >= sb[-1]:
            sb.pop()
        else:
            sj.pop()
    
    if sj:
        print('S')
    elif sb:
        print('B')
    else:
        print('C')