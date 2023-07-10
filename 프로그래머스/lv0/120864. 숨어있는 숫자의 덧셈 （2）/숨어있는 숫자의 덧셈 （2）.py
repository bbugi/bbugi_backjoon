def solution(my_string):
    answer = 0
    
    s = my_string.lower()
    
    alpha = [chr(i) for i in range(97, 123)]
    
    for a in alpha:
        s = s.replace(a, ' ')
    
    num_list = list(map(int, s.split()))
    
    answer = sum(num_list)
    
    return answer