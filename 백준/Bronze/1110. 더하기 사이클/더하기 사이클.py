n = int(input())  
original = n  
count = 0 

while True:
    a = n // 10  
    b = n % 10  
    sum_digits = a + b  
    n = (b * 10) + (sum_digits % 10)  
    count += 1 
    
    if n == original: 
        break

print(count) 
