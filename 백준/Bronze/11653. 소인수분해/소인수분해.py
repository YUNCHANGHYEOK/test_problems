import sys
input = sys.stdin.readline
N = int(input().strip())

k = 2

while N>1:
    if N%k ==0:
        
        while N%k == 0:
            print(k)
            N//=k
    k+=1
    

            