a,b = map(int,input().split())

arr = list(map(int,input().split()))

prefix = [0 for _ in range(a+1)]

for i in range(a):
    prefix[i+1] = prefix[i] + arr[i]

answer = []

for j in range(b,a+1):
    answer.append(prefix[j]-prefix[j-b])

print(max(answer))