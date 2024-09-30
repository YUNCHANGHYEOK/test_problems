import sys
input = sys.stdin.readline
N = int(input().strip())
list = []

for i in range(N):
    list.append(int(input().strip()))

a = sorted(list)

for j in a:
    print(j)

