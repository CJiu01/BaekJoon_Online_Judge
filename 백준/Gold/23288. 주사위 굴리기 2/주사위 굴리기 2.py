from collections import deque

def move_dice(dice, move):
    mapping = [
        [0,4,2,5,3,1],
        [3,0,1,2,4,5],
        [0,5,2,4,1,3],
        [1,2,3,0,4,5]
    ]
    dice[:] = [dice[i] for i in mapping[move]]
        
def switch_opposite_dir(d):
    if d<=1:
        d+=2
    else:
        d-=2
    return d
        
def forward(current_loc):
    x,y,d = current_loc
    dx,dy = x+dir[d][0], y+dir[d][1]
    
    if not (0<=dx<N and 0<=dy<M):
        d = switch_opposite_dir(d)
        dx, dy = x+dir[d][0], y+dir[d][1]

    return dx, dy, d

def calculate_score(board, current_loc):
    x,y = current_loc[0],current_loc[1]
    score = board[x][y]
    q = deque([[x,y]])
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    times = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx, dy = x+dir[i][0], y+dir[i][1]
            if 0<=dx<N and 0<=dy<M and (not visited[dx][dy]) and board[dx][dy]==score:
                q.append((dx,dy))
                visited[dx][dy] = True
                times += 1
                
    ans = score * (times+1)
    return ans

def set_next_dir(A,B,d):
    if A>B:
        d = (d+1)%4
    elif A<B:
        d = (d-1)%4
    return d     

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dir = [(0,1),(1,0),(0,-1),(-1,0)]
current_loc = [0,0,0]
dice = [2,1,5,6,4,3]
floor = 3
ans = 0

while K>0:
    # 1) 이동방향으로 1칸 이동 / 칸 없다면 반대로 1칸 이동
    current_loc[:] = forward(current_loc)
    move_dice(dice, current_loc[2])

    # 2) (x,y) 점수 획득
    ans += calculate_score(board, current_loc)
    
    # 3) A,B 비교해 다음 이동방향 결정
    x, y = current_loc[0], current_loc[1]
    current_loc[2] = set_next_dir(dice[floor], board[x][y], current_loc[2])

    K -= 1

print(ans)