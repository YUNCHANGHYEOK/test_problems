import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

prefix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

result = 0

for i in range(n):
    left_sum = arr[i] * i - prefix_sum[i]
    right_sum = (prefix_sum[n] - prefix_sum[i + 1]) - arr[i] * (n - i - 1)
    result += left_sum + right_sum

print(result)
