def solution(before, after):
    b_list = list(before)
    a_list = list(after)
    
    b_list.sort()
    a_list.sort()
    
    if b_list == a_list:
        return 1
    else:
        return 0