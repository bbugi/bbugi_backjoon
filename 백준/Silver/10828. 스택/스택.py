import sys
input = sys.stdin.readline

n = int(input()) 
stack = []
for _ in range(n):
    input_ord = input().split() # 자동으로 리스트로 받아낸다.
    # print(input_ord)
    order = input_ord[0]
    # print(order)
    
    if order == 'push':
        stack.append(input_ord[1])
        
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
            
    elif order == 'size':
        print(len(stack))
        
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])