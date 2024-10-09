import sys
input = sys.stdin.readline

N = int(input().strip())
S = set()

for i in range(N):
    a = input().strip().split()
    
    if len(a) > 1:
        v = int(a[1])
    
    
    if a[0] == 'add':
        S.add(v)
        
    elif a[0] == 'remove':
        if len(S) == 0:
            continue
        S.remove(v)
        
    elif a[0] == 'check':
        if v in S:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if v in S:
            S.remove(v)
        else:
            S.add(v)
            
    elif a[0] == 'all':
        S = set(range(1,21))
        
        
    elif a[0] == 'empty':
        S.clear()
                
                
                