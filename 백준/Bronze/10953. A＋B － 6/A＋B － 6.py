n = int(input())  # 첫 번째 입력에서 입력받을 줄의 수를 받음

for _ in range(n):
    a, b = map(int, input().split(','))
    print(a + b)
