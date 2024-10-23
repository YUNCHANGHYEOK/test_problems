N = int(input())  # 입력 받기

for i in range(1, N + 1):
    # 공백 출력
    print(' ' * (N - i), end='')
    # 별 출력
    print('*' * (2 * i - 1))
