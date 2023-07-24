n = int(input())
wh = list()
d = {}

for i in range(n):
    wh.append(tuple(map(int, input().split())))

for i in range(n):
    d[i] = 1
    for j in range(n):
        if i == j :
            pass
        else:
            if (wh[i][0] < wh[j][0]) and (wh[i][1] < wh[j][1]) :
                # print(i,j, wh[i][0],wh[i][1], wh[j][0],wh[j][1])
                d[i] += 1

print(*d.values())