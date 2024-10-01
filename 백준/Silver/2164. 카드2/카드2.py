import sys
input = sys.stdin.readline
from collections import deque

dq = deque()
N = int(input().strip())

for i in range(1,N+1):
    dq.append(i)
    
def one(dq):
    dq.popleft()
    a = dq.popleft()
    dq.append(a)
    #print(dq)
    

while 1:
    if len(dq) == 1:
        print(dq[0])
        break
    
    one(dq)
