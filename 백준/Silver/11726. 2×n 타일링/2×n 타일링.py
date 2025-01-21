a = int(input())
dp = [0]*a

if a == 1:
    print(1)
    exit()
elif a == 2:
    print(2)
    exit()

dp[0] = 1
dp[1] = 2

for i in range(2, a):
    dp[i] = (dp[i-1] + dp[i-2]) %10007
    
print(dp[a-1])
