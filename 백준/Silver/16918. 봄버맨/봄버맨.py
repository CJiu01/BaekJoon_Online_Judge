import sys
input = sys.stdin.readline

def check_time(N,time):
    if N == time:
        return True
    else:
        return False
    
def make_bomb(R,C,board):
    target = [[False]*C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                target[i][j] = True
            else:
                board[i][j] = 'O'      
    return target

def explode(board, target,R,C):
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for i in range(R):
        for j in range(C):
            if target[i][j]:
                board[i][j] = '.'
                for d in range(4):
                    dx, dy = i+dir[d][0], j+dir[d][1]
                    if 0<=dx<R and 0<=dy<C:
                        board[dx][dy] = '.'

def solve():
    R, C, N = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    time = 1
    
    while True:    
        if check_time(N, time):
            break
        target = make_bomb(R,C,board)

        time += 1
        if check_time(N, time):
            break
        
        explode(board, target, R, C)
        time += 1

    return board


def main():
    answer = solve()
    for i in answer:
        print(*i, sep='',end='')

if __name__ == '__main__':
    main()