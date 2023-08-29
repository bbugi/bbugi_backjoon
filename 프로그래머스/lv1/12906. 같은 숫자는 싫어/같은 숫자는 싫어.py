def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for idx in range(1,len(arr)):
        
        if arr[idx-1] != arr[idx] :
            answer.append(arr[idx])
        else:
            pass
    
        
    
    return answer