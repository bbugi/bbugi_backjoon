import re

while True:
    bracket = [] # 괄호 수집
    # sq_bracket = [] # 대괄호 수집
    sentence = input().split('.')
    sen = re.sub("[a-zA-Z ]", "", sentence[0])
    
    if len(sentence[0]) == 0:
        break
    
    elif sentence[0] == ' ':
        print('yes')
    
    else:
        for i in sen:
            if i == '(' or i == ')' or i == '[' or i == ']':
                bracket.append(i)
                for j in range(1, len(bracket)):
                    # print('여긴가?',bracket[j-1:j+1])
                    # print('이거는?', ''.join(bracket[j-1:j+1]))
                    if ''.join(bracket[j-1:j+1]) == '()' :
                        bracket.pop()
                        bracket.pop()
                    elif ''.join(bracket[j-1:j+1]) == '[]' :
                        bracket.pop()
                        bracket.pop()
                    # print('결과?', bracket)
            # elif i == '[' or i == ']' :
            #     sq_bracket.append(i)
            #     for j in range(1, len(sq_bracket)):
            #         if ''.join(sq_bracket[j-1:j+1]) == '[]' :
            #             sq_bracket.pop()
            #             sq_bracket.pop()
            #         else:
            #             pass
                    # print('[]결과는?', sq_bracket)
                            
        # print(bracket)
        if len(bracket) == 0:
            print('yes')
        else:
            print('no')