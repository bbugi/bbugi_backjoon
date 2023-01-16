full = [[0] * 100 for i in range(100)]

import sys
input = sys.stdin.readline

result = 0
for _ in range(4):
    temp = list(map(int, input().split()))
    for i in range(temp[0], temp[2]):
        for j in range(temp[1], temp[3]):
            if full[i][j] == 0:
                full[i][j] = 1
                result += 1
            else:
                pass
print(result)