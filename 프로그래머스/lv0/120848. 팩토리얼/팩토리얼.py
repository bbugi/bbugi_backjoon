def solution(n):
    answer = 0
    ans = 1    
    for i in range(1, 11):
        ans *= i
        if n >= ans :
            answer = i
    return answer