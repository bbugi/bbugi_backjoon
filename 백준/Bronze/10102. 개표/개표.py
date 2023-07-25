n = int(input())
string = list(input())
a = 0
b = 0
for s in string:
    if s == 'A':
        a += 1
    else:
        b += 1
        
if a > b : print('A')
elif a < b : print('B')
else: print('Tie')