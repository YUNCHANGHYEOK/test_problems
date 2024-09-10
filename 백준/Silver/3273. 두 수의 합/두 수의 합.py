a = int(input())

b = list(map(int,input().split(' ')))

c = int(input())

count  = 0
seen = set()

for i in b:
    if c-i in seen:
        count += 1
    seen.add(i)
    
print(count)