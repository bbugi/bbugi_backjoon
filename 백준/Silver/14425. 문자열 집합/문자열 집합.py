n, m = map(int, input().split())

n_list = []
for _ in range(n):
    n_list.append(input())
    
# print(n_list)
cnt = 0
for _ in range(m):
    if input() in n_list:
        cnt += 1
print(cnt)