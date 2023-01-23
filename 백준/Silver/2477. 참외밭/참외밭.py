from collections import deque

k = int(input())

a_list = deque()
b_list = deque()
for i in range(6):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    
while True:
    if a_list[0] == a_list[2] and a_list[1] == a_list[3]:
        small = (b_list[1] * b_list[2])
        big = (b_list[4] * b_list[5])
        break
    else:
        a_list.rotate(-1)
        b_list.rotate(-1)
        
print((big - small) * k)