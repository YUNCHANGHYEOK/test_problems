import sys
input = sys.stdin.readline


N = int(input().strip())

a = list(map(int,input().strip().split(' ')))
x = 0
count = 0

for i in a:
    if i == 1:
        continue

    for j in range(2,i):

        if i % j == 0:
            x += 1

    if x == 0:
        count += 1

    x = 0
            
            

print(count)

