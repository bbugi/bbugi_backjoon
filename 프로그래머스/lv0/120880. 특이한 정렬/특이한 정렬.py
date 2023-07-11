def solution(numlist, n):
    anslist = []
    answer = []
    
    for i in numlist :
        anslist.append(i-n)
        
    for i in sorted(anslist, key=lambda x : [abs(x), -x]):
        answer.append(numlist[anslist.index(i)])
    
    return answer