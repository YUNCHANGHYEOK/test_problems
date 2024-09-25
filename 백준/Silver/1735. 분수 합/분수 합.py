import sys
import math #gcd , lcm
input = sys.stdin.readline
N,a = map(int,input().strip().split(' '))
M,b = map(int,input().strip().split(' '))

lcm = math.lcm(a,b)

one = N*(lcm // a)
two = M*(lcm // b)

son = one+two
mother = lcm

gcd =math.gcd(son,mother)

son //= gcd
mother //= gcd
print(son, mother)



    