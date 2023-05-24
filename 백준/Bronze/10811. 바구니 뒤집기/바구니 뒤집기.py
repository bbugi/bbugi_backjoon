import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [ i+1 for i in range(n)]

# print(arr)

for num in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    # print(temp)
    temp.reverse()
    # print(temp)
    arr[i-1:j] = temp

print(*arr)