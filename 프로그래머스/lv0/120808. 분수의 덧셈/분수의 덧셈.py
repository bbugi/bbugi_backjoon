def solution(denum1, num1, denum2, num2):
    answer = []
    
    denum3 = int((denum1 * num2) + (denum2 * num1))
    num3 = int((num1 * num2))
    
    for i in range(1, num3+1):
        if denum3 % i == 0 and num3 % i == 0:
            denum4 = int(denum3/i)
            num4 = int(num3/i)
            
    answer.append(denum4)
    answer.append(num4)
    
    return answer