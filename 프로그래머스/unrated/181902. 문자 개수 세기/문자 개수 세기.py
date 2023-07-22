def solution(my_string):
    answer = [0] * 52
    alp = [chr(i).upper() for i in range(97, 123)]
    alp.extend([chr(i) for i in range(97,123)])
    
    for i in range(len(alp)) :
        for s in my_string :
            if s == alp[i]:
                answer[i] += 1
        
    return answer