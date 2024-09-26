import sys
input = sys.stdin.readline
N = int(input().strip())

a = list(map(int,input().strip().split(' ')))

print(max(a)*min(a))