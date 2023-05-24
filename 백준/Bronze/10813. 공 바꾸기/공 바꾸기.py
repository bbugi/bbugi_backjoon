import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [ i+1 for i in range(n)]

for num in range(m): # n번 반복하여 숫자를 받음
    i, j = map(int, input().split()) # i와 j 바구니의 값을 바꿔야 한다
    
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr)