#import sys
#input = sys.stdin.readline
#N = int(input().strip())
#list = []
#for i in range(N):
#    list.append(int(input()))
    
    
#sort_list = sorted(list)

#for i in sort_list:
#    print(i)

 
#입력크기가 너무 커서 sort 대신 계수정렬을 활용해야함
import sys

input = sys.stdin.readline
N = int(input().strip())

# 1부터 10000까지의 숫자 빈도 수를 저장할 리스트 생성
count = [0] * 10001

# 입력된 숫자에 해당하는 인덱스의 값을 1 증가시킴
for _ in range(N):
    num = int(input().strip())
    count[num] += 1

# 각 숫자를 빈도만큼 출력
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
