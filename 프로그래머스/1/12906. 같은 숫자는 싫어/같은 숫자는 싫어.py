def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in arr:
        if i in answer:
            if answer[-1] == i:
                continue
            else:
                answer.append(i)
        elif i not in answer:
            answer.append(i)
    
    
    
        
        
    return answer