import sys
input = sys.stdin.readline


n, k = map(int, input().split())

oly = []
for i in range(n):
    # 국가, 금, 은, 동
    oly.append(list(map(int, input().split())))   
# print(oly)

oly.sort(key= lambda x : (x[1], x[2], x[3]), reverse=True)
# print(oly)

for i in range(n):
    if oly[i][0] == k: 
        index = i

for i in range(n):
    if oly[index][1:] == oly[i][1:]:
        print(i + 1) 
        break 