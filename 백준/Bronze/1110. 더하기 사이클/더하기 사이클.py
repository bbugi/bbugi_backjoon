import sys
input = sys.stdin.readline

n = int(input())
ans = n
count = 0

while True:
    n1 = n // 10
    n2 = n % 10
    n3 = (n1+n2) % 10
    # num = int(str(n2)+str(n3))
    num = n2 * 10 + n3
    n = num
    count += 1
    if num == ans:
        break
    continue
print(count)