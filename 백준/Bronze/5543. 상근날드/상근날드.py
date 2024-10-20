li = []
for i in range(5):
    
    a = int(input())
    li.append(a)
buger = min(li[0:3])
drink = min(li[3:5])

print(int(buger) + int(drink)-50)
