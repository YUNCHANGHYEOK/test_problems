import sys
input = sys.stdin.readline

a,b = map(int,input().strip().split())
see = []
hear = []

for i in range(a+b):
    if i<a:
        see.append(input().strip())
    else:   
        hear.append(input().strip())
    
result = list(set(see) & set(hear))

print(len(result))
print('\n'.join(sorted(result)))   
