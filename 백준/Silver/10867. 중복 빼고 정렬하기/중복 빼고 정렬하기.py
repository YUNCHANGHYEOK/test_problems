
a = input()
b = list(map(int, input().split()))
d = sorted(set(b)) 
for j in d:
    print(j,end=' ')    
    
