import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * n

for num1 in range(m):
    i, j, k = map(int, input().split())

    for num2 in range(i-1, j):
        arr[num2] = k

print(*arr)