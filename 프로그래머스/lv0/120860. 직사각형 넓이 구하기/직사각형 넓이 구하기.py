def solution(dots):
    answer = 0
    
    h = abs(dots[0][0] - dots[1][0])
    if h == 0:
        h = abs(dots[0][0] - dots[2][0])
    v = abs(dots[0][1] - dots[1][1])
    if v == 0:
        v = abs(dots[0][1] - dots[2][1])
    
    answer = h * v
    return answer