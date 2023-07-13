def solution(n):
    ans = 0
    if n % 2 != 0:
        for i in range(1, n+1) :
            if i % 2 != 0:
                ans += i
        return ans
    else:
        for i in range(1, n+1) : 
            if i % 2 == 0 :
                ans += i*i
        return ans