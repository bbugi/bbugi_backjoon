def n2ten (num, n) :
    result = []

    while num > 0 :
        m = num % n # 나머지 -> n진법의 값이 나옴
        num = num // n 
        # result.append(m)
        result.insert(0, m) # result 리스트에 0인덱스 위치에 m을 추가하는 함수
    return result

ans = [i for i in range(10)]

alp = [chr(s).upper() for s in range(97,123)]
# print(alp)

ans.extend(alp)
# print(ans[35])

num, n = map(int, input().split())
result = n2ten(num, n)

for i in result :
    print(ans[i], end='')