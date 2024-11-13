import sys
input = sys.stdin.readline

a = int(input().strip())
b  = []

for _ in range(a):
    cnt = 0
    n = list(input().strip())
    balance = True
    for i in n:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1            
        if cnt < 0:
            balance = False
            break
    
    if balance and cnt == 0:
        b.append('YES')
    else:
        b.append('NO')
        
for i in b:
    print(i)

    
