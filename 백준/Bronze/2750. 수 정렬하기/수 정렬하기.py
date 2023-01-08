n = int(input())
num = []
for _ in range(n):
    k = int(input())
    num.append(k)
    num.sort()
for i in range(len(num)):
    print(num[i])