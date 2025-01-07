import sys
input = sys.stdin.readline

# 입력 받기
a, b = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 질의 처리
answer = []
for _ in range(b):
    start_index, end_index = map(int, input().split())
    # 구간 합 계산
    result = prefix_sum[end_index] - prefix_sum[start_index - 1]
    answer.append(result)

# 결과 출력
print("\n".join(map(str, answer)))
