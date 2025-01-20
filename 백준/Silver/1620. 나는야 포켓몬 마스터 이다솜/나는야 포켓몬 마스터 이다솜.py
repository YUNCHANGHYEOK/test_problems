a,b = map(int, input().split())
num = {}
name = {}

for i in range(1,a+1):
    c = input().strip()
    num[c] = i
    name[i] = c
    
answer = []


for _ in range(b):
    d = input().strip()
    
    if d.isdigit():
        answer.append(name[int(d)])
    else:
        answer.append(num[d])

print("\n".join(map(str, answer)))