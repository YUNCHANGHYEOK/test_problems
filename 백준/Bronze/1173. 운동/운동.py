N, m, M, T, R = map(int, input().split())
c = m
time = 0
e = 0

if m + T > M:
    print(-1)
else:
    while e < N:
        if c + T <= M:
            c += T
            e += 1
        else:
            c = max(m, c - R)
        time += 1
    print(time)