a = int(input())
dp = [0]*11

dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4,11):        
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
answer = []        
for j in range(a):
    b = int(input())
    answer.append(dp[b])
    
print("\n".join(map(str,answer)))
        
         