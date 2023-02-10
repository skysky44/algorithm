T = int(input())
for t in range(1, T + 1):
    words = input()
    for word in words:
        if words.count(word) == 2:
            pass
        else:
            print(f'#{t} No')
            break
    else:
        print(f'#{t} Yes')
