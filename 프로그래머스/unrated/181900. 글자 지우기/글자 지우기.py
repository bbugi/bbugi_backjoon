def solution(my_string, indices):
    answer = ''
    
    str_idx = [i for i in range(len(my_string))]
    
    for i in indices :
        for s in str_idx :
            if i == s:
                str_idx.remove(s)
                
    for s in str_idx :
        answer += my_string[s]
        
    return answer