N = int(input())  # 입력값 N
F = int(input())  # 입력값 F

base_N = (N // 100) * 100  # N의 마지막 두 자리를 00으로 만든 값

for i in range(100):  # 00~99 범위 탐색
    if (base_N + i) % F == 0:  # F로 나누어 떨어지는지 확인
        print(f"{i:02d}")  # 두 자리 형식으로 출력
        break
