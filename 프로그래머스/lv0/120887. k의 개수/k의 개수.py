def solution(i, j, k):
    cnt = 0
    num_list = []
    for n in range(i, j+1) :
        num_list.extend(map(int, list(str(n))))
        
    return num_list.count(k)