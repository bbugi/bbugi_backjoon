import sys
input = sys.stdin.readline

n = int(input())

fibo_list = [0] * 91 
# print(fibo_list)

fibo_list[1] = 1
fibo_list[2] = 1
for i in range(3, len(fibo_list)):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[n])