n = int(input())

for i in range(2*n-1):
    if i < n:
        # print(f'위치확인 i = {i}, n = {n}', end=' ')
        print(' ' * i + '*' * (2*(n-i)-1))
    else: # i = 6 7 8 9
        # print(f'위치확인 i = {i}, n = {n}', {n-i})
        print(' ' * (2*(n-1)-i) + '*' * (2*(i-n)+3))