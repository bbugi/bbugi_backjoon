from collections import deque

n, k = map(int, input().split())

num_deque = deque(i for i in range(2, n+1))
clr_list = []

while True:
    pop_num = num_deque.popleft()
    clr_list.append(pop_num)
    
    for next_num in list(num_deque):
        if next_num % pop_num == 0:
            clr_list.append(next_num)
            num_deque.remove(next_num)

    if len(num_deque) == 0:
        break

# print(clr_list)
print(clr_list[k-1])