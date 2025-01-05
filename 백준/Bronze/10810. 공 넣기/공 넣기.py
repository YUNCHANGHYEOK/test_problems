# 입력 받기
n, m = map(int, input().split())  # 바구니 개수 n, 작업 횟수 m
baskets = [0] * n  # 바구니 초기화 (모두 0으로 설정)

for _ in range(m):
    i, j, k = map(int, input().split())  # 작업 범위 i, j와 공 번호 k
    for idx in range(i - 1, j):  # i-1부터 j-1까지에 공 k를 넣음
        baskets[idx] = k

# 결과 출력
print(*baskets)
