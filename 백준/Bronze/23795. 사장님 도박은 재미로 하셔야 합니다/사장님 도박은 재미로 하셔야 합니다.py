import sys

total = 0  # 합 저장

while True:
    n = int(sys.stdin.readline())  # 입력 받기
    if n == -1:
        break  # -1이면 종료
    total += n  # 합산

print(total)
