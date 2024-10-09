import sys
input = sys.stdin.readline

N = int(input().strip())
my_list = []
for i in range(N):
    a,b = input().strip().split()
    a = int(a)
    b = list(b)

    
    for j in range(len(b)):
        my_list.append(b[j]*a)

        
    print("".join(my_list))
    my_list =[]
    

    