# 팩토리얼 미사용해서 팩토리얼 풀어보기
n = int(input())
# n= 0
# num = 1
# for i in range(1, n+1):
#     print(i)
#     num *= i
# print(num)

# 팩토리얼 재귀함수 사용해보기
def facto(n):
    if n <= 1 :
        return 1
    return n * facto(n-1)
print(facto(n))