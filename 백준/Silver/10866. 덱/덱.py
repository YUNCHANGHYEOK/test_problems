import sys
from collections import deque

dq = deque()


input = sys.stdin.readline
N = int(input().strip())

for i in range(N):
    miss = input().strip().split(' ')

    if len(miss) == 1:
        if miss[0] == 'front':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq[0])

        if miss[0] == 'back':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[-1])

        if miss[0] == 'size':
            print(len(dq))

        if miss[0] == 'empty':
            if len(dq) == 0:
                print(1)
            else:
                print(0)

        if miss[0] == 'pop_front':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq.popleft())
                
        if miss[0] == 'pop_back':
            if len(dq) == 0:
                print(-1)

            else:
                print(dq.pop())
                
            

    if len(miss) == 2:
        
        if miss[0] == 'push_front':
            dq.appendleft(int(miss[1]))
        else:
            dq.append(int(miss[1]))




