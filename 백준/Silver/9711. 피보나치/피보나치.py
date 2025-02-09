a = int(input())

answer  = []

dp = [0]*(10001)

dp[0] = 1
dp[1] = 1

for i in range(2,10001):
    dp[i] = dp[i-1] + dp[i-2]


for i in range(a):
    b,c = map(int,input().split())

    result = dp[b-1] % c

    answer.append(result)


for i in range(len(answer)):
    print(f'Case #{i+1}:',answer[i])






