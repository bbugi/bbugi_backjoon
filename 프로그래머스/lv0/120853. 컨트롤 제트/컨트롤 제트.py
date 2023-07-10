def solution(s):
    answer = 0
    
    s_list = list(s.split())
    num_list = []
    
    for i in s_list :
        if i != 'Z' :
            num_list.append(int(i))
        if i == 'Z' :
            num_list.pop()
    answer = sum(num_list)
            
    return answer