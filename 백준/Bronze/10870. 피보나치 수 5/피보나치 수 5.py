n = int(input())
def fibo5(n):
    if n <= 1:
        return n
    return fibo5(n-1) + fibo5(n-2)
print(fibo5(n))