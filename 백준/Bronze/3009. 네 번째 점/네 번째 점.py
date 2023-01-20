import sys
input = sys.stdin.readline
square_x = [0] * 1001
square_y = [0] * 1001

for i in range(3):
    x, y = map(int, input().split())
    square_x[x] += 1
    square_y[y] += 1
    
print(square_x.index(1), square_y.index(1))