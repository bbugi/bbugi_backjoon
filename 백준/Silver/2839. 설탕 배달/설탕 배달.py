n = int(input())
def bag(n):
    ans = []
    for x in range(0, n//5+1):
        for y in range(0, n//3+1):
            if n - 5*x - 3*y == 0:
                ans.append(x+y)

    if len(ans) == 0:
        return -1
    else:
        return min(ans)

print(bag(n))