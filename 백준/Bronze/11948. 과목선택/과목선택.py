li = []
for i in range(6):
    a = int(input())
    li.append(a)
    
#print(li)
li.remove(min(li[0:4]))
print(sum(li[0:3])+max(li[3:5]))

