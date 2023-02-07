k, s, n = input().split()

location = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    '8': 0, '7': 1, '6': 2, '5': 3,
    '4': 4, '3': 5, '2': 6, '1': 7
}
dic_move = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}
king = (location[k[1]], location[k[0]])
stone = (location[s[1]], location[s[0]])

for i in range(int(n)):

    direction = input()
    move = dic_move[direction]

    moved_king = tuple(sum(elem) for elem in zip(king, move))

    if 0 <= moved_king[0] <= 7 and 0 <= moved_king[1] <= 7:
        if moved_king != stone:
            king = moved_king
        else:
            moved_stone = tuple(sum(elem) for elem in zip(stone, move))

            if 0 <= moved_stone[0] <= 7 and 0 <= moved_stone[1] <= 7:
                king = moved_king
                stone = moved_stone
print(chr(king[1]+65)+str(8-king[0]),
      chr(stone[1]+65)+str(8-stone[0]), sep='\n')