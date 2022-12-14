ans = [1, 1, 2, 2, 2, 8]
# len(ans)

piece = list(map(int, input().split(' ')))
# print(piece)

num = []
for i in range(len(ans)):
    num.append(ans[i]-piece[i])
# print(num)
print(f'{num[0]} {num[1]} {num[2]} {num[3]} {num[4]} {num[5]}')