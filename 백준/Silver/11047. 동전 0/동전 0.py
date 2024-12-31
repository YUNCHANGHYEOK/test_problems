import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = []
sum = K
num = 0

# 동전 값 입력받기
for _ in range(N):
    a = int(input())
    l.append(a)

# 내림차순으로 정렬
l.sort(reverse=True)

# 동전 개수 계산
for coin in l:
    if sum == 0:
        break
    if coin <= sum:
        num += sum // coin
        sum %= coin

print(num)
