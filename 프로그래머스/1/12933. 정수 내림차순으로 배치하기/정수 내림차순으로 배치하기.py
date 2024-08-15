def solution(n):
    answer = 0
    
    l = list(str(n))
    l.sort(reverse = True)
    
    answer = ''.join(l)
    
    return int(answer)