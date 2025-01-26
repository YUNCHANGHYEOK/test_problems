N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

a_set = set(a)
answer = []
for i in b:
    if i in a_set:
        answer.append(1)
    else:
        answer.append(0)
        
print(' '.join(map(str,answer)))