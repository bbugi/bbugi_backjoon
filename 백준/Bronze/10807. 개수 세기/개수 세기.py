import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
v = int(input())

def search_num(n, b, v):
    return(b.count(v))

print(search_num(n, b, v))