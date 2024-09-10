 #1920
 
a = int(input())
b = list(map(int,input().split(' ')))

b1 = set(b)
c = int(input())
d = list(map(int,input().split(' ')))

for i in d:
    if i in b1:
        print(1)
    else :
        print(0)
    
