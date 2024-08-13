def solution(x, n):
    answer = []
    k = 1
    for i in range(n):
        answer.append(x*k)
        k+=1
    return answer