from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(n):
    input_ord = input().split()
    order = input_ord[0]

    if order == 'push':
        d.append(input_ord[1])
        
    elif order == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
            
    elif order == 'size':
        print(len(d))
        
    elif order == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0]) # deque의 경우도 앞의 값이 빠지면 인덱스가 0으로 되는걸...??
    elif order == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])   