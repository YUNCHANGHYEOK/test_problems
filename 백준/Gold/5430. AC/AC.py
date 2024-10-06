import sys
input = sys.stdin.readline

T = int(input().strip())

def AC(p,n,my_list):
    
    
    reverse = False
    
    for i in p:
        if i == 'R':
            reverse = not reverse
            #print('R실행완료')
            
        elif i == 'D':
            if len(my_list) == 0:
                return 'error'
                
            if reverse:
                my_list.pop()  # 뒤집힌 상태라면 마지막 요소 제거
            else:
                my_list.pop(0)  # 일반 상태라면 첫 번째 요소 제거
            #print('D실행완료')
                
                
    if reverse:
        my_list = my_list[::-1]
        
                
    return my_list
                

for i in range(T):
    p = list(input().strip())
    n = int(input().strip())
    my_list = eval(input().strip())
    a = AC(p,n,my_list)
    if a == 'error':
        print(a)
    else:
        print(f"[{','.join(map(str, a))}]")
           