import sys
input = sys.stdin.readline

n = int(input())

a = 0
b = 1

while n > 0:
    a, b = b, a+b
    n -= 1

print(a)