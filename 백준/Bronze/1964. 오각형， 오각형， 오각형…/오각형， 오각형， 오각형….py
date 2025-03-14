import sys

n = int(sys.stdin.readline().strip())

points = 5

for i in range(2, n + 1):
    points += (i * 3 + 1)

print(points % 45678)
