# 입력을 받음
numbers = list(map(int, input().split()))

# 조건 확인
if numbers == list(range(1, 9)):
    print("ascending")
elif numbers == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")
