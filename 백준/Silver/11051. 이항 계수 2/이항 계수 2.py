import sys
input = sys.stdin.readline
import math

N,M = map(int,input().strip().split())

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(binomial_coefficient(N, M) % 10007)
