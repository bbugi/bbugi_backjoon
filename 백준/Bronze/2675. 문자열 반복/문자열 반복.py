for _ in range(int(input())):
    r, s = input().split()

    r = int(r)
    s = list(s)

    for a in s:
        print(r*a, end='')
    print()