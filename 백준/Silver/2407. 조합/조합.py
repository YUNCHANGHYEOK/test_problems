import sys
input = sys.stdin.readline


N,M = map(int,input().strip().split())
son = 1
mom = 1

for i in range(M):
    son *= (N-i)

for j in range(M):
    mom *= M-j
#print(son)
#print(mom)
print(son // mom)

