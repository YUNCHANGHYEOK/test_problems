#10773
import sys
input = sys.stdin.readline

a = int(input().strip())
li = []


def push(a):
    li.append(a)
    return a

def pop(li):    
    if empty(li) == 1:
        return -1
    else: 
        a = li.pop()
        return a

def size(li):
    return len(li)

def empty(li):
    if len(li) == 0:
        return 1
    else:
        return 0
    
def top(li):
    if empty(li):
        return -1
    else:
        return li[-1]


for i in range(a):
    c = input().strip().split(' ')
    if len(c) == 1:
        if c[0] == 'top':
            print(top(li))
        if c[0] == 'size':
            print(size(li))
        if c[0] == 'empty':
            print(empty(li))
        if c[0] == 'pop':
            print(pop(li))
            
            
    else:
        num = int(c[1])
        if c[0] == 'push':
            push(num)
        
        
        