import sys
input = sys.stdin.readline


a = int(input())
c = []
for i in range(a):
    b = int(input())
    c.append(b)
    
d = sorted(c,reverse=True)

for i in range(a):
    print(d[i])