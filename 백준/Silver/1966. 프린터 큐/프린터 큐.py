from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    pop_num = []

    queue = deque([i+1 for i in range(n)])
    find_num = queue[m]
    imp_q = deque(map(int, input().split()))

    while True:
        if len(imp_q) == 0 :
            break
    
        max_idx = imp_q.index(max(imp_q))

        if max_idx != 0:
            queue.rotate(-1)
            imp_q.rotate(-1)
            continue

        elif max_idx == 0:
            pop_num.append(queue.popleft())
            imp_q.popleft()
            continue

    for num in pop_num :
        if find_num == num :
            print(pop_num.index(num) + 1)