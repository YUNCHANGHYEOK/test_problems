def solution(n):
    answer = []
    
    a = str(n)
    b = list(a)
    c = b[::-1]
    d = list(map(int,c))
    return d