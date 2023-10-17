
N = int(input())
best_scores = []

for i in range(N):
    # 각 사람의 카드를 읽어와서 리스트로 변환
    cards = [*map(int, input().split())]

    # 각 사람이 가질 수 있는 가장 큰 일의 자리 수를 저장할 변수
    max_digit = 0

    # 세 장의 카드를 선택하여 합의 일의 자리 수 계산
    for one in range(5):
        for two in range(one + 1, 5):
            for three in range(two + 1, 5):
                # 세 장의 카드의 합의 일의 자리 수 계산
                temp = (cards[one] + cards[two] + cards[three]) % 10
                # 현재까지의 최대 일의 자리 수보다 크면 갱신
                if max_digit < temp:
                    max_digit = temp

    # 현재 사람의 최대 일의 자리 수를 리스트에 추가
    best_scores.append(max_digit)

# 가장 큰 일의 자리 수 중에서 가장 큰 값을 찾음
best = max(best_scores)

# 이긴 사람의 번호를 찾아 출력
for i in range(N - 1, -1, -1):
    if best == best_scores[i]:
        print(i + 1)
        break