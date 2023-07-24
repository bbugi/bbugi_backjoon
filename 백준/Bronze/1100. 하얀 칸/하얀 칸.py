board = []
cnt = 0

for i in range(8) :
    board.append(list(input()))
    for j in range(8) :
        if i % 2 == 0 and j % 2 == 0 :
            if board[i][j] == 'F' : 
                cnt += 1
        elif i % 2 != 0 and j % 2 != 0 :
            if board[i][j] == 'F' :
                cnt += 1
print(cnt)