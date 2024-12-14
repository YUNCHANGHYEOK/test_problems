import sys
input = sys.stdin.read

def solve():
    data = input().splitlines()
    for line in data:
        h1, m1, s1, h2, m2, s2 = map(int, line.split())
        start = h1 * 3600 + m1 * 60 + s1
        end = h2 * 3600 + m2 * 60 + s2
        diff = end - start

        h = diff // 3600
        m = (diff % 3600) // 60
        s = diff % 60
        print(h, m, s)

solve()
