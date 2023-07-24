color = ["black", "brown","red","orange",
         "yellow","green","blue","violet",
         "grey","white"]

ans = ''

for i in range(3):
    s = input()
    if s in color:
        if i == 0:
            if s == 'black':
                pass
            else:
                ans += str(color.index(s))

        elif i == 1:
            ans += str(color.index(s))
        
        else:
            ans += '0' * color.index(s)

if set(ans) == 0 :
    print(0)
else:    
    print(int(ans))