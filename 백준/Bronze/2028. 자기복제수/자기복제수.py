T = int(input())

for _ in range(T):
    n = int(input()) 
    square = n * n 
    if str(square).endswith(str(n)):
        print("YES")
    else:
        print("NO")
