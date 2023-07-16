def solution(keyinput, board):
    answer = []
    x = y = 0
    
    b_x = board[0] // 2
    b_y = board[1] // 2
    
    for key in keyinput :
        if key == 'left' :
            x -= 1
        if key == 'right' :
            x += 1
        if key == 'up' :
            y += 1
        if key == 'down' :
            y -= 1

        if x > b_x :
            x = b_x
        if x < b_x * -1 :
            x = b_x * -1
        if y > b_y :
            y = b_y
        if y < b_y * -1 :
            y = b_y * -1
            
    answer = [x,y]      

    return answer