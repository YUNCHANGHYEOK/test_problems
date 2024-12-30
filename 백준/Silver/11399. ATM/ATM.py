a = int(input())
b = list(map(int,input().split()))

b.sort()

sum = 0
current_sum = 0

for i in b:
    current_sum += i
    sum += current_sum

#print(b)
print(sum)