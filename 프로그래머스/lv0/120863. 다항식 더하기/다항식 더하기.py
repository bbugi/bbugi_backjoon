def solution(polynomial):
    answer = ''
    
    x_cnt = 0
    n_cnt = 0

    lp = list(map(str, polynomial.split()))

    for l in lp :
        if 'x' in l :
            if l == 'x' :
                x_cnt += 1
            else :
                x_cnt += int(l.replace('x',''))

        elif l != '+' :
            n_cnt += int(l)

    if x_cnt == 0 :
        answer = (f'{n_cnt}')
    elif n_cnt == 0:
        if x_cnt == 1:
            answer = 'x'
        else:
            answer = (f'{x_cnt}x')
    else:
        if x_cnt == 1:
            answer = (f'x + {n_cnt}')

        else:
            answer = (f'{x_cnt}x + {n_cnt}')

    
    return answer