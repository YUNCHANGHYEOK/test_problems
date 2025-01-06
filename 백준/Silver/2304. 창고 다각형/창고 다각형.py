N = int(input())
arr = []

for i in range(N):
    a = list(map(int, input().split()))
    arr.append(tuple(a))  # 튜플로 변환

# 첫 번째 값을 기준으로 정렬
arr.sort(key=lambda x: x[0])

#print(arr)

# 최대 높이, 길이 구하기
L_max, H_max = max(enumerate(arr), key=lambda x: x[1][1])


#왼쪽에서 오른쪽 면적 계산
area = 0
c_h = 0

for i in range(L_max+1):
    c_h = max(c_h,arr[i][1])
    if i < L_max:
        area += c_h*(arr[i+1][0]- arr[i][0])

#오른쪽에서 왼쪽 면적 계산

c_h = 0 
for i in range(len(arr)-1,L_max-1,-1):
    c_h = max(c_h,arr[i][1])
    if i > L_max:
        area += c_h*(arr[i][0] - arr[i-1][0])

area += c_h
print(area)
