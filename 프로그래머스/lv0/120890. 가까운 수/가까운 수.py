def solution(array, n):
    min = 100
    answer = 0
    array.sort()
    for i in array :
        num = abs(i - n)
        if min > num :
            min = num
            answer = i
    return answer