import sys
input = sys.stdin.readline



while 1 :
    a,b = map(int,input().strip().split())
    if a == 0 and b == 0:
        break
    else:
        if a<b or a == b:
            print('No')
        elif a > b: 
            print('Yes')