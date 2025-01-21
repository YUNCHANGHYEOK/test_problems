a = int(input())
n = [int(input()) for _ in range(a)]

if a == 1:
    print(n[0])
elif a == 2:
    print(n[0] + n[1]) 
else:
    dp = [0] * a
    dp[0] = n[0]
    dp[1] = n[0] + n[1]
    dp[2] = max(n[0] + n[2], n[1] + n[2])

    for i in range(3, a):
        dp[i] = max(dp[i-2] + n[i], dp[i-3] + n[i-1] + n[i])

    print(dp[-1]) 
