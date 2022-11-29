s = list(list(map(int, input().split())) for _ in range(9))
max_num = max(map(max, s))

for i in range(len(s)):
    for j in range(len(s)):
        if s[i][j] == max_num:
            mx_i = i+1
            mx_j = j+1
print(max_num)
print(f'{mx_i} {mx_j}')