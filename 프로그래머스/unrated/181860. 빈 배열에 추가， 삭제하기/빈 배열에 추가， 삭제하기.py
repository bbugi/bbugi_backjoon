def solution(arr, flag):
    answer = []
    for i in range(len(flag)) :
        tmp = []
        if flag[i] == True:
            answer.extend([arr[i]] * (arr[i]*2))
        elif flag[i] == False:
            answer = answer[:-arr[i]]
    return answer