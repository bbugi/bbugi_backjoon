def solution(babbling):
    answer = 0
    
    list = ["aya", "ye", "woo", "ma"]
    
    list2 = []
    
    for i in range(len(list)):
        list2.append(list[i])
        for j in range(len(list)):
            if list[i] != list[j]:
                list2.append(list[i]+list[j])
            for k in range(len(list)):
                if (list[i] != list[j]) and (list[j] != list[k]) and (list[k] !=list[i]):
                    list2.append(list[i]+list[j]+list[k])
                for m in range(len(list)):
                    if (list[i] != list[j]) and (list[i] != list[k]) and (list[i] !=list[m]):
                        if (list[j] != list[k]) and (list[j] != list[m]):
                            if (list[k] != list[m]):
                                list2.append(list[i]+list[j]+list[k]+list[m])
    
    for x in babbling:
        if x in list2:
            answer += 1
    
    return answer