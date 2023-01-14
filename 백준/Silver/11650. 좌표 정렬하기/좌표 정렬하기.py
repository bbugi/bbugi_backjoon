import sys
input = sys.stdin.readline

n = int(input())
m = []

for _ in range(n):
    x, y = map(int, input().split())
    m.append([x,y])

num_sort = sorted(m, key = lambda x : (x[0], x[1]))
for i in range(n):
    print(*num_sort[i], end='\n')