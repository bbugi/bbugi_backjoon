import sys
input = sys.stdin.readline

for _ in range(3) :
    n = int(input())
    ans = 0
    for i in range(n) :
        ans += int(input())
    if ans == 0 : 
        print('0')
    elif ans > 0 :
        print('+')
    else :
        print('-')