fibo = [0, 1]
for i in range(2, 10001):
    fibo.append(fibo[i-1]+fibo[i-2])
    
# print(fibo)

t = int(input())

for i in range(t):
    p, q = map(int, input().split())
    
    print(f"Case #{i+1}:", fibo[p]%q)