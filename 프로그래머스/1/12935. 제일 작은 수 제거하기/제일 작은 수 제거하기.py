def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        return answer
    a = arr.index(min(arr))
    del arr[a]
    
    
    return arr