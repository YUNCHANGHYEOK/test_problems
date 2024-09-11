#10773

a = int(input())
li = []


def push(a):
    li.append(a)


def pop():    
    if li: #리스트가 비어있지 않는다면
        li.pop()


for i in range(a):
    b = int(input())
    if b == 0:
        pop()
    else:
        push(b)

print(sum(li))