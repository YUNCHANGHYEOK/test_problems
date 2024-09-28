import sys
input = sys.stdin.readline

def pl(N):
    for i in range(int(len(N)/2)):
        if N[i] != N[len(N)-1-i]:
            print('no')
            return
        
    print('yes')
            

while True:
    N = list(map(int,input().strip()))
    if N[0] == 0:
        break
    pl(N)




