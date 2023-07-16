def solution(board):
    n = len(board)
    xy = []
    num = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                xy.append([i,j])
                
    for x, y in xy :
        for a in range(-1, 2) :
            for b in range(-1, 2) :
                if 0 <= x+a < n and 0 <= y+b < n:
                    board[x+a][y+b] = 1
    for i in range(n):
        num += sum(board[i])
        
    return n*n - num