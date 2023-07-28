def solution(arr):
    answer = []
    i = 0
    len_arr = len(arr)
    while i < len(arr):
        if i < len_arr :
            if len(answer) == 0:
                answer.append(arr[i])
                i += 1
            else:
                if answer[-1] == arr[i] :
                    answer.pop()
                    i += 1
                else:
                    answer.append(arr[i])
                    i += 1
            
    if answer == []:
        answer.append(-1)
    return answer