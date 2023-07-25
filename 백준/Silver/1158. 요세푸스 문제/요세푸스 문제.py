from collections import deque

n, k = map(int,input().split())
yose = deque([i+1 for i in range(n)])

print('<', end='')
for i in range(n) :
    yose.rotate(-k+1)
    
    if i != n-1 :
        print(yose.popleft(), end=', ')
    else:
        print(yose.popleft(), end='')

print('>')