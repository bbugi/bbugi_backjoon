# 단어 입력받아 대문자 알파벳으로 변환하여 리스트 담기
word = list(input().upper())
# print(word)

# 해당 리스트의 유일한 알파벳이 어떤것인지 추출하여 리스트에 담기
uni = list(set(word))
# print(uni)

# 유일한 알파벳이 원래 단어에 몇개 들어있는지 개수 확인
# 파이썬 리스트의 특정 요소 개수 구하기 -> ""리스트명.count(특정 요소)"" 사용
cnt = []
for i in uni:
    # print(word.count(i))
    cnt.append(word.count(i))
    
# 유일 알파벳 개수 추출한 리스트의 최댓값 확인
max(cnt)

# 유일한 알파벳 최댓값이 2개 이상일때 '?' 출력
if cnt.count(max(cnt)) >= 2:
    print('?')
# 아니라면 cnt리스트에서 최댓값이 위치한 인덱스 번호 추출하여 uni 리스트에 적용하여 문자 추출
else:
    print(uni[cnt.index(max(cnt))])
