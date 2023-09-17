t = int(input())

for _ in range(t):
    results = {}
    
    for _ in range(16):
        team1, team2, score1, score2 = input().split()
        score1 = int(score1)
        score2 = int(score2)

        if score1 > score2:
            results[team1] = results.get(team1, 0) + 1
        else:
            results[team2] = results.get(team2, 0) + 1

    winner = max(results, key=results.get)
    print(winner)