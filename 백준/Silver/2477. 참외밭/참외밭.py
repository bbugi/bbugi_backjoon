from collections import deque

k = int(input())

a_list = deque()
b_list = deque()
for i in range(6):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

# print(a_list)
# print(b_list)

while True:
    if a_list[0] == a_list[2] and a_list[1] == a_list[3]:
        small = (b_list[1] * b_list[2])
        break
    else:
        a_list.rotate(-1)
        b_list.rotate(-1)

# print(a_list)
# print(b_list)

max1 = []
for i in range(1,5):
    if a_list.count(i) == 1:
        # print(i) # 2, 4
        max1.append(b_list[a_list.index(i)])
# print(max1)

big = max1[0] * max1[1]

print((big - small) * k)