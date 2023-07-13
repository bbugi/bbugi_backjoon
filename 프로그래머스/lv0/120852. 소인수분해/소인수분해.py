def solution(n):
    answer = []
    start_num = 2

    while start_num <= n :
        if n % start_num == 0:
            if start_num not in answer :
                answer.append(start_num)
            n = n // start_num
            
        else :
            start_num += 1
    return answer
