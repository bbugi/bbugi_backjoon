import sys
input = sys.stdin.readline

n = int(input())
ans = n
num_cnt = 0
while True:
    if num_cnt == 0:
        n1 = n // 10 # 10의자리 수
        n2 = n % 10 # 1의 자리 수
        k = n1 + n2
        k1 = k // 10
        k2 = k % 10
        n = int(str(n2) + str(k2))
        num_cnt += 1
        continue
    elif n != ans:
        n1 = n // 10 # 10의자리 수
        n2 = n % 10 # 1의 자리 수
        n = n1 + n2
        k = n1 + n2
        k1 = k // 10
        k2 = k % 10
        n = int(str(n2) + str(k2))
        num_cnt += 1
        continue
    else:
        print(num_cnt)
        break