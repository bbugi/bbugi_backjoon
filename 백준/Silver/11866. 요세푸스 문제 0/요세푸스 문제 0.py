from collections import deque
n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

print('<', end='')

for i in range(n):
    for j in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if i != n-1 :
        print(',', end=' ')
print('>')