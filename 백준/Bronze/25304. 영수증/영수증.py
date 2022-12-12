x = int(input())
n = int(input())
prices = []
for _ in range(n):
    a, b = map(int, input().split())
    prices.append(a*b)


if sum(prices) == x:
    print('Yes')
else:
    print('No')
    