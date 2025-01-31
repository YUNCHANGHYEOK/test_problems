import sys

n = int(sys.stdin.readline().strip())
files = [sys.stdin.readline().strip() for _ in range(n)]

pattern = list(files[0])

for i in range(len(pattern)):
    for j in range(1, n):
        if files[j][i] != pattern[i]:
            pattern[i] = '?'
            break

print("".join(pattern))
