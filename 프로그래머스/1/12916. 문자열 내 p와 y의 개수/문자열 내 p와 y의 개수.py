def solution(s):
    answer = True
    t = s.lower()
    
    b = 0
    c = 0
    for i in t:
        if i == 'p':
            b += 1
        elif i == 'y':
            c += 1
    if b == c:
        return True
    else:
        return False




