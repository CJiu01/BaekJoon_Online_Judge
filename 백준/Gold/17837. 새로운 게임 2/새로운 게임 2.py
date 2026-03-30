

def set_board(horses):
    b = [[[] for _ in range(N)] for _ in range(N)]
    for i,h in enumerate(horses):
        x,y,d = h
        b[x][y].append(i)
    
    return b
    
    
def move_white(x,y,dx,dy,target):
    t = board[x][y].index(target)
    tmp = board[x][y][t:]
    board[x][y] = board[x][y][:t]
    board[dx][dy] += tmp
    
    for j in tmp:
        horses[j][0],horses[j][1] = dx,dy

def move_red(x,y,dx,dy,target):
    t = board[x][y].index(target)
    
    tmp = board[x][y][t:]
    tmp.reverse()
    board[x][y] = board[x][y][:t]
    board[dx][dy] += tmp

    for j in tmp:
        horses[j][0],horses[j][1] = dx,dy

def opposite_dir(d):
    if d==0: return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

def move_blue(x,y,target,d):
    d = opposite_dir(d)
    horses[target][2] = d
    dx = x+dir[d][0]
    dy = y+dir[d][1]
    
    if 0<=dx<N and 0<=dy<N and color[dx][dy]!=2:
        
        t = board[x][y].index(target)
        tmp = board[x][y][t:]
        board[x][y] = board[x][y][:t]
        
        if color[dx][dy] == 1:
            tmp.reverse()
            
        board[dx][dy] += tmp
        
        for j in tmp:
            horses[j][0],horses[j][1] = dx,dy
 
    return

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
horses = [list(map(lambda x:int(x)-1, input().split())) for _ in range(K)]    
    
dir = [(0,1),(0,-1),(-1,0),(1,0)]
board = set_board(horses)

ans = 0
while ans<=1000:
    ans += 1
    end = False
    
    for i in range(K):
        x,y,d = horses[i]
        dx = x+dir[d][0]
        dy = y+dir[d][1]

        if 0<=dx<N and 0<=dy<N:
            c = color[dx][dy]
            if c==0:
                move_white(x,y,dx,dy,i)
            elif c==1:
                move_red(x,y,dx,dy,i)
            else:
                move_blue(x,y,i,d)
        else:
            move_blue(x,y,i,d)
            
        ex,ey = horses[i][0], horses[i][1]
        if len(board[ex][ey])>=4:
            end = True
            break
    if end:
        break
    
    
if ans<=1000:
    print(ans)
else:
    print(-1)