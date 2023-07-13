def solution(a, d, included):
    answer = 0
    numbers = list( a+(d*i) for i in range(len(included)))
    
    for i in range(len(included)) :
        if included[i] == True:
            answer += numbers[i]
    
    return answer