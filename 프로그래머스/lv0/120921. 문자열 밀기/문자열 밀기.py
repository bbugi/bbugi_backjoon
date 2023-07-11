from collections import deque
def solution(A, B):
    answer = 0
    
    a = deque(A)
    b = deque(B)
    
    if a == b :
        return 0
    else:
        for i in range(len(a)):
            if a != b :
                a.rotate(1)
                answer += 1
        if answer == len(a) :
            return -1
        
    return answer