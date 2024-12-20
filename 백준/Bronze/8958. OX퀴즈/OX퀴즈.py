n = int(input())
for _ in range(n):
    quiz = input()
    score, total = 0, 0
    for ch in quiz:
        if ch == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
