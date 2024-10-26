N = int(input())

# 윗부분 (1 ~ N)
for i in range(1, N + 1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)

# 아랫부분 (N-1 ~ 1)
for i in range(N - 1, 0, -1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
