from collections import deque
N = int(input())
skills = list(map(int, input().split()))
start_cards = deque()
last_cards = [card for card in range(N, 0, -1)]
for skill in skills[::-1]:
    if skill == 1:
        start_cards.appendleft(last_cards.pop())
    elif skill == 2:
        temp = start_cards.popleft()
        start_cards.appendleft(last_cards.pop())
        start_cards.appendleft(temp)
    elif skill == 3:
        start_cards.append(last_cards.pop())
print(*list(start_cards))
