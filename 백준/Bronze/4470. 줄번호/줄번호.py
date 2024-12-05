n = int(input())
lines = [input() for _ in range(n)]
for i, line in enumerate(lines, 1):
    print(f"{i}. {line}")
