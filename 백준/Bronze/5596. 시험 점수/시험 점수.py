import sys
input = sys.stdin.readline

a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

#print(sum(a))
#print(sum(b))

if sum(a) > sum(b):
    print(sum(a))
elif sum(a) < sum(b):
    print(sum(b))
else:
    print(sum(a))

