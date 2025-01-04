from itertools import combinations

# 9명의 난쟁이 키 입력받기
heights = [int(input()) for _ in range(9)]

# 7명을 선택하는 모든 조합 확인
for comb in combinations(heights, 7):
    if sum(comb) == 100:  # 키의 합이 100인 경우
        result = sorted(comb)  # 정렬
        for height in result:  # 결과 출력
            print(height)
        break
