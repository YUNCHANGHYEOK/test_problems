def recur(num):
    if num == M: 
        print(*arr)
        return
    for i in range(1, N + 1):
        if i not in arr:  # 중복 체크
            arr.append(i)
            recur(num + 1)
            arr.pop()

N, M = map(int, input().split())
arr = []
recur(0)
