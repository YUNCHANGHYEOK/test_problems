L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

math_days = -(-A // C)  
korean_days = -(-B // D) 

print(L - max(math_days, korean_days))
