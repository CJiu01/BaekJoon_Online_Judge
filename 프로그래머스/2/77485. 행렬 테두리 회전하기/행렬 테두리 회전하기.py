def solution(rows, columns, queries):
    answer = []
    board = [[i*columns+j for j in range(1,columns+1)] for i in range(rows) ]
    
    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1
        
        for i in range(c1, c2+1):
            stack.append(board[r1][i])
            if len(stack)==1:
                continue
            board[r1][i] = stack[-2]

        for j in range(r1+1, r2+1):
            stack.append(board[j][c2])
            board[j][c2] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[r2][k])
            board[r2][k] = stack[-2]
  
        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][c1])
            board[l][c1] = stack[-2]

        answer.append(min(stack))
    return answer 