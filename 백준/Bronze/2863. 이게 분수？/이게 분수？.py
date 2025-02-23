A, B = map(int, input().split())
C, D = map(int, input().split())

# 4가지 회전의 값 계산
values = [
    (A / C) + (B / D),  # 0회 회전
    (C / D) + (A / B),  # 1회 회전
    (D / B) + (C / A),  # 2회 회전
    (B / A) + (D / C)   # 3회 회전
]

# 최대값이 위치한 인덱스 찾기
best_rotation = values.index(max(values))

# 출력
print(best_rotation)
