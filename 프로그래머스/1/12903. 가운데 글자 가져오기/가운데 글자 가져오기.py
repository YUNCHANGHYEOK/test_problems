def solution(s):
    a = len(s)
    if a % 2 == 1:
        return s[int(a / 2)]    
    else:
        
        return s[int(a/2)-1:int(a/2)+1]