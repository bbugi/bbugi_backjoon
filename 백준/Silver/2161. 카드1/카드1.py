import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q =  deque( i for i in range(1,n+1))
q_list = []

for i in range(n):
    q_list.append(q.popleft())
    if len(q) != 0:
        q.append(q.popleft())
    else:
        pass

print(*q_list)