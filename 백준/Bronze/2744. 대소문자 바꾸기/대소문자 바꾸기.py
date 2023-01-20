import sys
input = sys.stdin.readline

words = list(input().rstrip())
new = []

for word in words:
    if word.isupper() == True:
        word = word.lower()
    else:
        word = word.upper()
    new.append(word)
    
print(*new, sep='')