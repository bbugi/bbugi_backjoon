n = int(input())
s_list = []
for _ in range(n):
    s = list(input())
    if len(s_list) == 0:
        s_list = s
    else:
        for i in range(len(s)):
            if s_list[i] != s[i] :
                s_list[i] = '?'
print(*s_list, sep='')