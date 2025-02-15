n = int(input())  # 참가자 수
max_prize = 0  # 가장 큰 상금 저장

for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        prize = 10000 + a * 1000
    elif a == b or a == c:
        prize = 1000 + a * 100
    elif b == c:
        prize = 1000 + b * 100
    else:
        prize = max(a, b, c) * 100

    max_prize = max(max_prize, prize)

print(max_prize)
