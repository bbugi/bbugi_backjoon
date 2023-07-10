def solution(s):
    answer = ''
    
    s_list = list(s)
    s_list.sort()
    for i in s_list :
        if s_list.count(i) == 1:
            answer += i
    
    
    return answer