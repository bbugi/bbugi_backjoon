n = int(input())
books = {}

for i in range(n) :
    title = input()
    
    if title not in books.keys():
        books[title] = 1
    else:
        books[title] += 1
        
max_sell = max(books.values())

best_seller = []
for k, v in books.items() :
    if v == max_sell :
        best_seller.append(k)

best_seller.sort()

print(best_seller[0])