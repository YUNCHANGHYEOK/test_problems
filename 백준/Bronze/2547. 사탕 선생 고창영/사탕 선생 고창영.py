import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    sys.stdin.readline()
    n = int(sys.stdin.readline().strip())
    total = 0
    for _ in range(n):
        total += int(sys.stdin.readline().strip())
    print("YES" if total % n == 0 else "NO")