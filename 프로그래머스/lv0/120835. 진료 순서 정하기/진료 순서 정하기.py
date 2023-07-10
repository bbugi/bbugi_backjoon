def solution(emergency):
    answer = []
    e = emergency.copy()
    e.sort(reverse=True)
    
    for i in emergency:
        if i in e:
            answer.append(e.index(i) + 1)
    return answer