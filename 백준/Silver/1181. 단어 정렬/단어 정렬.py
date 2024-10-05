import sys
input = sys.stdin.readline 

n = int(input().strip())
    
my_list = []
for i in range(n):
    a = input().strip()
    
    my_list.append(a)
        
my_list = list(set(my_list))
    
sort_list = sorted(my_list,key= lambda x:(len(x),x))
[print(x) for x in sort_list]



    

