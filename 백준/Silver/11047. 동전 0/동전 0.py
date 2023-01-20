import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
count = 0
for _ in range(n):
    coins.append(int(input()))
coins.reverse()
# print(coins)

for coin in coins:
    count += k // coin
    k = k % coin

print(count)