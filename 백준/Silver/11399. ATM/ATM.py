n = int(input())

numbers = list(map(int, input().split()))

sorted_nums = sorted(numbers)
ans = 0

for i in range(n):
    ans += sum(sorted_nums[:i+1])
print(ans)