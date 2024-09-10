#10828

a = list(input())
#print(a)

b = [0]*26
c = ord('a')

for i in a:
    b[ord(i)-c] += 1    
print(' '.join(map(str,b)))



