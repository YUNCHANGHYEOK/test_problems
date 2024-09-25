import sys
import math #gcd , lcm
input = sys.stdin.readline
N = int(input().strip())

for i in range(N):
    a,b = map(int,input().strip().split(' '))
    print(math.lcm(a,b))
    