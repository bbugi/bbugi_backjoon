def solution(dots):
    answer = 0
    
    i = 0
    for j in range(1, len(dots)):
        dots1 = dots.copy()
        a = ((dots[i][1]-dots[j][1]) / (dots[i][0]-dots[j][0]))
        del dots1[j]
        del dots1[i]
        b = ((dots1[0][1]-dots1[1][1]) / (dots1[0][0]-dots1[1][0]))
        if a == b:
            answer =1

    return answer