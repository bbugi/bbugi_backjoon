an = ['a','e','i','o','u']
while True:
    count = 0
    sens = list(input().lower())

    if sens[0] == "#":
        break
    
    for sen in sens:
        if sen in an:
            count += 1
    print(count)