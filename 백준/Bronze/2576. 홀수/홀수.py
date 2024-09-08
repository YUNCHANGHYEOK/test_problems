li = []
for i in range(7):
    a = int(input())
    li.append(a)

li2 = []
sum = 0
for i in li:
    if(i%2 == 1):
        li2.append(i)
        sum += i
if len(li2) == 0:
    print(-1)
else:
        
    li2.sort()
    print(sum)
    print(li2[0])

