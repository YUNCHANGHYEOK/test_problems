
a,b = map(int,input().split())
c = {}
for _ in range(a):
    id,password = input().split()
    c[id] = password

#print(c)
result = []
for _ in range(b):
    d = input()
    result.append(c[d])    
    

print("\n".join(result))


