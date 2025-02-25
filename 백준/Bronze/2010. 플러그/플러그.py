import sys


N = int(sys.stdin.readline())  
total_holes = 0

for _ in range(N):
    total_holes += int(sys.stdin.readline())  


max_devices = total_holes - (N - 1)
print(max_devices)
