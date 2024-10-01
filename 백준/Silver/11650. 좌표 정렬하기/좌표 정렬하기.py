import sys
input = sys.stdin.readline

N = int(input().strip())
a = []

# 입력을 받아 리스트에 저장
for _ in range(N):
    a.append(tuple(map(int, input().strip().split())))

# 정렬된 리스트를 출력
for i in sorted(a):
    print(i[0], i[1])
