import sys

N = int(sys.stdin.readline().strip()) 
min_time = float('inf')  

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())  
    if A <= B:  
        min_time = min(min_time, A)  


print(min_time if min_time != float('inf') else -1)
