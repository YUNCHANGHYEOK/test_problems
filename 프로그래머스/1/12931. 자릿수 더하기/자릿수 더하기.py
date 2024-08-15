def solution(n):
    k = 0
    
    while n > 0:
        k += n % 10
        n = n //10
        
    
    

    return k