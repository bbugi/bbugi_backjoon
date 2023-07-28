def solution(strArr):   
    tmp = [0] * 31
    
    for i in range(len(strArr)) :
        tmp[len(strArr[i])] += 1
        
    return max(tmp)