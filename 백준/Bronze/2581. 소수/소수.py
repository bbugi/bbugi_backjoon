from collections import deque
import math

m = int(input())
n = int(input())

ans = deque([])

for i in range(m, n+1) :
    ans.append(i)
    # print(ans)
    for j in range(2, int(math.sqrt(i))+1) :
            if i % j == 0:
                ans.remove(i)
                break

if 1 in ans :
     ans.remove(1)

if len(ans) == 0 :
    print(-1)
else:
    print(sum(ans))
    print(ans[0])