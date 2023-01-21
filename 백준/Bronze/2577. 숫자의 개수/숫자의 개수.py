import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = (a * b * c)
num_l = [int(a) for a in str(num)]

count = [0] * 10
for i in range(10):
    for j in range(len(num_l)):
        if i == num_l[j]:
            count[i] += 1

print(*count, sep='\n')