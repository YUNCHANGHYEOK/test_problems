# 입력 받기
m = int(input())

# 공의 위치 (초기 위치는 1번 컵)
pos = 1

# 컵 교환 수행
for _ in range(m):
    a, b = map(int, input().split())
    # 현재 공이 a에 있으면 b로 이동
    if pos == a:
        pos = b
    # 현재 공이 b에 있으면 a로 이동
    elif pos == b:
        pos = a

# 결과 출력
print(pos)
