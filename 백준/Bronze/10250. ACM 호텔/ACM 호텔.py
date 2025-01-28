t = int(input())  
for _ in range(t):
    h, w, n = map(int, input().split())
    
    # 층수 계산
    floor = n % h
    if floor == 0:
        floor = h
        room = n // h
    else:
        room = n // h + 1
    

    print(f"{floor}{room:02}")
