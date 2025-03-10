def sigma_sum(A, B):
    # A가 B보다 크다면 교환
    if A > B:
        A, B = B, A
    # 등차수열 합 공식 사용
    return (B - A + 1) * (A + B) // 2

# 입력
A, B = map(int, input().split())

# 결과 출력
print(sigma_sum(A, B))
