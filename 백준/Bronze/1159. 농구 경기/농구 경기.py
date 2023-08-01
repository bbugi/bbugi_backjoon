import sys
input = sys.stdin.readline

n = int(input())
names = {}
ans=[]

for i in range(n) : 
    name = input()
    if name[0] not in names.keys() :
        names[name[0]] = 1
    else : 
        names[name[0]] += 1

for k, v in names.items() :
    if v >= 5 :
        ans.append(k)
        
if len(ans) > 0 :
    ans.sort()
    print(*ans, sep='')
else :
    print('PREDAJA')