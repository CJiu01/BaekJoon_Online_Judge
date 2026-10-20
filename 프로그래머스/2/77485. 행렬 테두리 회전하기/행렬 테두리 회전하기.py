def rotate(query):
    global board
    dir = ((0,1),(1,0),(0,-1),(-1,0))
    start_x, start_y, end_x, end_y = [x-1 for x in query]
    rotated = [b.copy() for b in board]
    res = []
   
    x,y = start_x, start_y
    for i in range(4):
        
        for j in range(101):
            dx, dy = x+dir[i][0], y+dir[i][1]
            if start_x<=dx<=end_x and start_y<=dy<=end_y:
                rotated[dx][dy] = board[x][y]
                res.append(board[x][y])
                x,y = dx,dy
            else:
                break
    board = [r.copy() for r in rotated]
    return min(res)

def solution(rows, columns, queries):
    global board
    answer = []
    board = [[i*columns+j for j in range(1,columns+1)] for i in range(rows) ]
    
    for query in queries:
        answer.append(rotate(query))

    return answer 