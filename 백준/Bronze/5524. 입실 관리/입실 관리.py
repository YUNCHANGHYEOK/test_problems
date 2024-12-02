# 입력받기
n = int(input())  
names = [input().strip() for _ in range(n)]

for name in names:
    print(name.lower())
