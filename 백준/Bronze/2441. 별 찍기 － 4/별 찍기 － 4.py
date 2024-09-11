#2441

a = int(input())
b = 0
for i in range(a,0,-1):
    print(' '*b,end='')
    print('*'*i)
    b+=1