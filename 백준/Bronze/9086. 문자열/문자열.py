import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    a = (input().strip())

    print(a[0]+a[-1])
    
        