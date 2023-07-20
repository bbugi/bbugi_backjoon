from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

num = []
base = deque([])
ans = []
sign = []

for i in range(n):
    base.append(int(input()))
    
i = 1
# print(base)

while True:

    if len(base) == 0 :
        print(*sign, sep='\n')
        break
    
    
    if len(num) > 0 :
        if base[0] == num[-1] :
            sign.append('-')
            ans.append(num.pop())
            base.popleft()
            continue
        if base[0] in num:
            print('NO')
            break
    
    if i not in num:
        sign.append('+')
        num.append(i)
        i += 1