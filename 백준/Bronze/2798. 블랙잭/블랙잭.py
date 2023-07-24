from itertools import combinations
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

ans = 0

check_list = list(combinations(numbers, 3))

for i in range(len(check_list)) :
    check_sum = sum(check_list[i])
    if m >= check_sum > ans :
        ans = check_sum
print(ans)