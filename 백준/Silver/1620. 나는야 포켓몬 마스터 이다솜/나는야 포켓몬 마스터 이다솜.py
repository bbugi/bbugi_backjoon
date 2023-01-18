import sys
input = sys.stdin.readline

n, m= map(int, input().split())

num_dict = {}

for i in range(n):
    num_dict[i+1] = input().rstrip()

name_dict = {value:key for key, value in num_dict.items()}

# print(num_dict)
# print(name_dict)


for i in range(m):
    find = input().rstrip()
    try: # 숫자 받았을 때
        print(num_dict.get(int(find)))
    except: # 문자 받았을 때 - value값으로 key 값 찾기
        print(name_dict.get(find))