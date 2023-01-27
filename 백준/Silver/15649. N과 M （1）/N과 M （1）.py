import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
    
lst = []
for i in range(1, n+1):
    lst.append(i)
    
# print(lst)
c = itertools.permutations(lst, m)
for num in c:
    num = ' '.join(map(str, num))
    print(num)