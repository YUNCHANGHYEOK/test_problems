a, b = map(int, input().split())

# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(a)]

# Prefix 배열 초기화 (1-based)
prefix = [[0 for _ in range(a + 1)] for _ in range(a + 1)]

# Prefix 배열 생성
for y in range(a):
    for x in range(a):
        prefix[y + 1][x + 1] = (
            prefix[y][x + 1]
            + prefix[y + 1][x]
            - prefix[y][x]
            + graph[y][x]
        )

# 쿼리 입력 받기
queries = [tuple(map(int, input().split())) for _ in range(b)]

# 결과 계산
result = []
for y1, x1, y2, x2 in queries:  # row와 column 순서로 처리
    answer = (
        prefix[y2][x2]
        - prefix[y1 - 1][x2]
        - prefix[y2][x1 - 1]
        + prefix[y1 - 1][x1 - 1]
    )
    result.append(answer)

# 결과 출력
for i in result:
    print(i)
