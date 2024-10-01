import sys
input = sys.stdin.readline

N = int(input().strip())
list1 = list(map(int,input().strip().split()))


M = int(input().strip())
list2 = list(map(int,input().strip().split()))



from collections import Counter

# list1의 빈도수 계산
counter = Counter(list1)

list3 = []

# list2의 각 요소에 대해 list1에서의 빈도수 찾기
for i in list2:
    list3.append(counter.get(i, 0))  # 해당 요소의 빈도수가 없으면 0을 반환

print(*list3)
