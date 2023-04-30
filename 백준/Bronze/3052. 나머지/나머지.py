s_list = [input() for _ in range(10)]
# print(s_list)

na_list = []
for i in range(len(s_list)):
    # print(s_list[i])
    # print(int(s_list[i])%42)
    na_list.append(int(s_list[i])%42)
    
# print(na_list)
print(len(list(set(na_list))))