import sys
input = sys.stdin.readline

def binary_search(n_list, search_value): 
    first, last = 0, n-1
    
    while first <= last:
        mid = (first + last) // 2

        if n_list[mid] == search_value:
            return True
        
        if n_list[mid] > search_value:
            last = mid - 1
        else:
            first = mid + 1

            
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
# print(n_list)

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    # print(m_list[i])
    if binary_search(n_list, m_list[i]) == True:
        print(1)
    else:
        print(0)