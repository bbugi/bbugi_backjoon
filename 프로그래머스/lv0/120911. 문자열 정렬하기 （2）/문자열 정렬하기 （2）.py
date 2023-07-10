def solution(my_string):
    mystr = list(my_string.lower())
    mystr.sort()
    answer = ''.join(mystr)
    return answer