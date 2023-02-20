# import math

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     print(n, m)    
#     cnt = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
#     print(cnt)

# ======= 팩토리얼 함수 만들어서 풀이하기

def s_factorial(n):
    num = 1
    for i in range(1, n+1):
        # print(i)
        num *= i
    return num

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    cnt = s_factorial(m) // (s_factorial(m-n) *(s_factorial(n)) )
    print(cnt)