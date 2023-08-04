import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()
    ans = 0
    if num == '0':
        break
    else :
        num_list = list(num)
        ans = len(num_list) + 1
        for nums in num_list:
            if nums == '0' :
                ans += 4
            elif nums == '1' :
                ans += 2
            else:
                ans += 3
    print(ans)