while True:
    n = int(input())
    ans = []
    
    if n == -1 :
        break
    else :
        for i in range(1, n) :
            if n % i == 0 :
                ans.append(i)
                
        if sum(ans) == n :
            print(n, '=', end=' ')
            for i in range(len(ans)) :
                if i < len(ans)-1 :
                    print(ans[i], '+', end=' ')
                else :
                    print(ans[i])
                    
        else :
            print(n, 'is NOT perfect.')