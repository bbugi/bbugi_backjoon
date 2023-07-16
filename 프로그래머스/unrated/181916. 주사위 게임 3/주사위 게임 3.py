def solution(a, b, c, d):
    numbers = [a, b, c, d]
    cnt = {}
    
    for i in numbers :
        if i in cnt.keys():
            cnt[i] += 1
        else:
            cnt[i] = 1
            
    if len(set(numbers)) == 1:
        return (1111 * numbers.pop())
    
    elif len(set(numbers)) == 4:
        return min(numbers)
    
    elif len(set(numbers)) == 2:
        if 3 in cnt.values():
            p = [k for k, v in cnt.items() if v == 3][0]
            q = [k for k, v in cnt.items() if v == 1][0]
            return ( (10 * p + q) ** 2)
        else:
            p, q = cnt.keys()
            return ((p+q) * abs(p-q))
        
    else:
        p = [k for k, v in cnt.items() if v == 2][0]
        q, r = [k for k in numbers if p != k]
        return (q * r)
    