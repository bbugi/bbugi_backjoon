def solution(myString):
    tmp = myString.split('x')
    answer = []
    
    for t in tmp:
        if t != '':
            answer.append(t)
    answer.sort()
    
    return answer