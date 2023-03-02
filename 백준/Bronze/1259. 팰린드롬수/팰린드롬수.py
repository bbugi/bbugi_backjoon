while True :
    n = int(input())
    # print(n)
    
    if n == 0 :
        break
    
    n_list = list(str(n))
    # print(n_list)
    
    m_list = n_list.copy()
    m_list.reverse()
    # print(m_list)
    
    if n_list == m_list :
        print('yes')
    else:
        print('no')