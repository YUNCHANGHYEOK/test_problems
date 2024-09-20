import sys
input = sys.stdin.readline


N= list(map(int,input().strip().split(' ')))
count = 0
li = []

a = max(N)
b = min(N)

for i in range(b+1,a):
    count += 1
    li.append(i)

print(count)
for i in li:
    print(i,end=' ')
