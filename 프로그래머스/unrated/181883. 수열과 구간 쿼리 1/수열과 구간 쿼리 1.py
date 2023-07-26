def solution(arr, queries):
    
    for q in range(len(queries)) :
        for i in range(len(arr)) :
            if queries[q][0] <= i <= queries[q][1] :
                arr[i] += 1
            
    return arr