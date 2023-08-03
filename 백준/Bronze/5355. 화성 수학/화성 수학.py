import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    fomula = list(map(str, input().split()))
    num = float(fomula[0])
    
    for i in range(1, len(fomula)) :
        if fomula[i] == '@' :
            num *= 3
        elif fomula[i] == '%' :
            num += 5
        elif fomula[i] == '#' :
            num -= 7
    
    print("{:.2f}".format(num))