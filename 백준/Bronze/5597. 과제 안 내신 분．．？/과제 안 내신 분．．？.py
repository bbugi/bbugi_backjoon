import sys
input = sys.stdin.readline

a = list(range(1,31))
# print(a)
for _ in range(28):
    n = int(input())
    a.remove(n)
    # print(n, a)
print(*a, sep='\n')