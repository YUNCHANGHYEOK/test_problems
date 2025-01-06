a = int(input())
arr = list(map(int, input().split()))


prefix = [0 for _ in range(a)]
prefix[0] = arr[0]

for i in range(1, a):

    prefix[i] = max(prefix[i-1] + arr[i], arr[i])

print(max(prefix))
