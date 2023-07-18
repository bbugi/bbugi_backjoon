t = int(input())
a_lst = []
b_lst = []

for i in range(t):
    a, b = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)

print((max(a_lst) - min(a_lst)) * (max(b_lst) - min(b_lst)))
