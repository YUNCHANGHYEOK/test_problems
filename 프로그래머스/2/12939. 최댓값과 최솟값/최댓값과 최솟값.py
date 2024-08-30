def solution(s):
    answer = ''
    t = []
    
    a = list(map(int,s.split(' ')))
    
    b = str(max(a))
    c = str(min(a))
    
    t.append(c)
    t.append(b)
    answer = ' '.join(t)
    
    return answer
