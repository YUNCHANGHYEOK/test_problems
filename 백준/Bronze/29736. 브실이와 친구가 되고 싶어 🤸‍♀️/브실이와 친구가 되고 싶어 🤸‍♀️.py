A, B = map(int, input().split())
K, X = map(int, input().split())

start = max(A, K - X)
end = min(B, K + X)

if start > end:
    print('IMPOSSIBLE')
else:
    print(end - start + 1)
