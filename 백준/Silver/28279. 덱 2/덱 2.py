import sys
from collections import deque

dq = deque()


input = sys.stdin.readline
N = int(input().strip())

for i in range(N):
    miss = input().strip().split(' ')

    if len(miss) == 1:
        if miss[0] == '7':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq[0])

        if miss[0] == '8':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[-1])

        if miss[0] == '5':
            print(len(dq))

        if miss[0] == '6':
            if len(dq) == 0:
                print(1)
            else:
                print(0)

        if miss[0] == '3':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq.popleft())
                
        if miss[0] == '4':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq.pop())
                
            

    if len(miss) == 2:
        
        if miss[0] == '1':
            dq.appendleft(int(miss[1]))
        elif miss[0] == '2':
            dq.append(int(miss[1]))



