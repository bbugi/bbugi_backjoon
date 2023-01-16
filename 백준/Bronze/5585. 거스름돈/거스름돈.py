import sys
input = sys.stdin.readline

money = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())
coin = 0
for i in money: 
    coin += n // i
    n %= i

print(coin)