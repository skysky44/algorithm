x, y = map(int, input().split())
game = {}
game[1, 2] = 'B' # B가 이기는 경우 1
game[2, 3] = 'B' # B가 이기는 경우 2
game[3, 1] = 'B' # B가 이기는 경우 3
game[1, 3] = 'A' # A가 이기는 경우 1
game[2, 1] = 'A' # A가 이기는 경우 2
game[3, 2] = 'A' # A가 이기는 경우 3
print(game[x, y])