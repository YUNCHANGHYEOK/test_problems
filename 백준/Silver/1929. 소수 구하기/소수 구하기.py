import sys
import math

input = sys.stdin.read
M, N = map(int, input().split())

# 소수를 저장할 배열을 True로 초기화
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False로 설정

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# 결과 출력
for num in range(M, N + 1):
    if is_prime[num]:
        print(num)