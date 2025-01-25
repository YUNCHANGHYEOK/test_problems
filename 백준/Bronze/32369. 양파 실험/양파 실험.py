N,A,B = map(int,input().split())

a,b = 0,0
for i in range(N):
    a += A
    b += B
    tmp = 0
    if a < b:
        tmp = a
        a = b
        b = tmp
        
    if a == b:
        b -= 1

print(a+1,b+1)