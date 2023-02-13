import sys
input = sys.stdin.readline
N = int(input())
cards = {}
cards_list = list(map(int, input().split()))
for i in cards_list:
    cards[i] = cards.get(i, 0) + 1
M = int(input())
targets = list(map(int, input().split()))
for j in targets:
    print(cards.get(j, 0), end=' ')
