n, m = map(int, input().split())
card=[0]
for i in range(n):
    card.append(int(input()))
for i in range(1, m+1):
    for j in range(1, n):
        if card[j] % i > card[j+1] % i:
            tmp = card[j]
            card[j] = card[j+1]
            card[j+1] = tmp
            
print(*card[1:], sep='\n')
                