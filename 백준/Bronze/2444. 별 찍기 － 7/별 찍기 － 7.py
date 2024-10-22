n = int(input())

# 윗부분 피라미드
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아랫부분 피라미드
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
