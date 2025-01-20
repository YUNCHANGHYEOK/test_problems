a = int(input())
dp = [0]*101

dp[1] = 1
dp[2] = 1
dp[3] = 1


for i in range(4,101):        
    dp[i] = dp[i-3] + dp[i-2]
        
answer = []        
for j in range(a):
    b = int(input())
    answer.append(dp[b])
    
print("\n".join(map(str,answer)))
        
         