import sys
input = sys.stdin.readline

n = int(input())

m_list = []
for _ in range(n):
    x, y = map(str, input().split())
      # 리스트 변수 = input().split() 
      # x, y = input().split()

    m_list.append([int(x), y])

# print(m_list)
sorted_m = sorted(m_list, key = lambda x : x[0])
# sorted_m = sorted(m_list)

for i in sorted_m:
    print(*i)