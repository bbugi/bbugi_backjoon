angles = []
for i in range(3):
    angles.append(int(input()))

if sum(angles) != 180:
    print('Error')

elif set(angles).pop() == 60:
    print('Equilateral')

else :
    if len(set(angles)) == 3:
        print('Scalene')
    else:
        print('Isosceles')