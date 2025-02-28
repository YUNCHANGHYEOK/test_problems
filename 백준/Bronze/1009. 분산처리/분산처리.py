def last_digit(a, b):
    # 각 숫자별 1의 자리 패턴 정의
    patterns = {
        0: [10],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    
    # a의 1의 자리 숫자
    last_digit_of_a = a % 10
    # 해당 숫자의 패턴 가져오기
    pattern = patterns[last_digit_of_a]
    # 패턴의 길이
    pattern_length = len(pattern)
    # b를 패턴의 길이로 나눈 나머지 (1을 빼고 계산 후 다시 1을 더함)
    index = (b - 1) % pattern_length
    # 결과 반환
    return pattern[index]

# 테스트 케이스 수 입력
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(last_digit(a, b))
