import sys
input = sys.stdin.readline

n, m= map(int, input().split())

# 포켓몬 도감 만들기
num_dict = {}
for i in range(n):
    num_dict[i+1] = input().rstrip()
name_dict = {value:key for key, value in num_dict.items()}
# 기존에 받은 num_dict의 키값과 밸류값을 반대로하여 새로운 딕셔너리로 생성
# items() - 사전 데이터(키와 값을 쌍)을 리턴 (dict_items)
# for 반복문을 활용해 사전 데이터를 쉽게 출력할 수 있다.

# print(num_dict) key(숫자) : value(문자) 형태의 딕셔너리
# print(name_dict) key(문자) : value(숫자) 형태의 딕셔너리

# 도감에서 값 찾기
for i in range(m): # key값으로 value값 찾기 -> 딕셔너리명.get(key값)
    find = input().rstrip()
    try: # 숫자 받았을 때
        print(num_dict.get(int(find)))
    except: # 문자 받았을 때
        print(name_dict.get(find))