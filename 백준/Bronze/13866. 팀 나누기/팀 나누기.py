scores = list(map(int, input().split()))
scores.sort()
team1 = scores[0] + scores[3]
team2 = scores[1] + scores[2]
print(abs(team1 - team2))
