t = int(input())
for _ in range(t):

# 딕셔너리에 키 값에 해당하는 값이 있으면 1씩 추가하는 코드
    counts = {}
    n = int(input())
    for _ in range(n):
        name, w_type = map(str, input().split())
        # print(name, w_type)
        if w_type not in counts:
            counts[w_type] = 1
        else:
            counts[w_type] += 1

    c_list = list(counts.values())
    # print(c_list)
    for i in range(len(c_list)):
        c_list[i] = c_list[i]+1
    
    ans = 1
    for i in c_list:
        ans *= i
    print(ans - 1)