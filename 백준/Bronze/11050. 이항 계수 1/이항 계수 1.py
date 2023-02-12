from itertools import combinations

n, k = map(int, input().split())

item = [i for i in range(n)]
# print(item)

print(len(list(combinations(item, k))))