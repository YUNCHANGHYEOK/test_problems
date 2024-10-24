# N 입력 받기
N = int(input())

# 역삼각형 출력
for i in range(N):
    print(' ' * i + '*' * (2*(N-i)-1))

# 삼각형 아래 부분 출력
for i in range(1, N):
    print(' ' * (N-i-1) + '*' * (2*i+1))
