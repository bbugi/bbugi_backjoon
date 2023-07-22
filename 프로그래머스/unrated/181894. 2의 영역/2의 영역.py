def solution(arr):
    answer = []
    idx = []
    
    for i in range(len(arr)) :
        if arr[i] == 2:
            idx.append(i)
    if len(idx) == 0:
        answer.append(-1)
    else:
        answer.extend(arr[idx[0] : idx[-1]+1])
        
    return answer