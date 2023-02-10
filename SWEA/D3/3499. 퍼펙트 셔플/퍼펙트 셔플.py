# import sys
from collections import deque
# sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    all_cards = deque(input().split())
    cards_1 = deque()
    cards_2 = deque()
    result = []
    if N % 2 == 0:
        for _ in range(N//2):
            cards_1.append(all_cards.popleft())
        cards_2 = all_cards
    else:
        for _ in range((N//2)+1):
            cards_1.append(all_cards.popleft())
        cards_2 = all_cards
    while len(cards_2) != 0:
        result.append(cards_1.popleft())
        result.append(cards_2.popleft())
    if len(cards_1) != 0:
        result.append(cards_1.popleft())
    print(f'#{t} ', end='')
    print(*result)
