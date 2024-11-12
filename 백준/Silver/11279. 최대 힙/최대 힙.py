import heapq
import sys
input = sys.stdin.readline

heap = []
printheap = []  

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            printheap.append(0)
        else:
            printheap.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))
        
for i in printheap:
    print(i)