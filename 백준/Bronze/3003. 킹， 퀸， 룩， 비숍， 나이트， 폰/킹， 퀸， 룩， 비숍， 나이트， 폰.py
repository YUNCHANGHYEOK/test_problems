# 필요한 말의 개수를 리스트로 정의
required_pieces = [1, 1, 2, 2, 2, 8]

# 입력받은 현재 말의 개수를 리스트로 저장
current_pieces = list(map(int, input().split()))

# 부족한 개수 계산 후 출력
missing_pieces = [required - current for required, current in zip(required_pieces, current_pieces)]
print(*missing_pieces)